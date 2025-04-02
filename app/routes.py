from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from user_agents import parse
from app.utils.articleContent import articlesDictionary
from .models import ArticleAnalytics
from . import db
import json

main = Blueprint('main', __name__, template_folder="templates")

@main.route('/')
def home_page():
    return render_template('home.html', articles = articlesDictionary)

@main.route('/article')
def show_article():
    # article number
    article_number = request.args.get('article_id')

    if not article_number:
        return redirect(url_for('main.home_page'))

    articleData = articlesDictionary.get(f"article_{article_number}")

    return render_template("article.html", articleData=articleData, article_number=article_number)

@main.route('/dashboard')
def dashboard():
    articles = ArticleAnalytics.query.all()

    article_list = [
        {
            "article_id": a.article_id,
            "clicks": a.clicks,
            "time_spent": a.time_spent,
            "browser_counts": a.browser_counts,
            "os_counts": a.os_counts,
            "headline": articlesDictionary.get(f'article_{a.article_id}').get("headline")
        }
        for a in articles
    ]

    return render_template("analytics.html", articles=articles, articles_json=article_list)

@main.route('/update-analytics', methods=['POST'])
def update_analytics():
    request_data = request.get_json()

    article_id = str(request_data.get('article_id'))
    event_type = request_data.get('event_type')

    if event_type == "click":
        user_agent_string = request.headers.get('User-Agent', '')
        ua = parse(user_agent_string)

        browser = ua.browser.family
        os = ua.os.family

        # update the click count by 1 for the specific article
        article_obj = ArticleAnalytics.query.filter_by(article_id=article_id).first()
        article_obj.clicks += 1
        print(browser)
        print(os)
        article_obj.browser_counts[browser] = article_obj.browser_counts.get(browser, 0) + 1
        article_obj.os_counts[os] = article_obj.os_counts.get(os, 0) + 1

        db.session.commit()
        return jsonify({"success": True}), 200
    
    return jsonify({"error": True}), 400

@main.route('/track-time', methods=['POST'])
def track_time():
    try:
        data = request.get_json(force=True)  # force parsing
    except:
        data = json.loads(request.data)

    article_id = str(data.get('article_id'))
    time_spent = float(data.get('time_spent', 0.0))

    article = ArticleAnalytics.query.filter_by(article_id=article_id).first()
    if not article:
        return jsonify({"error": "Article not found"}), 404

    article.time_spent += time_spent
    db.session.commit()

    return jsonify({"message": "Time tracked"}), 200



@main.route('/test-insert')
def insert_test():
    record = ArticleAnalytics(
        article_id='1',
        clicks=34,
        time_spent=12.5,
        browser_counts={"Chrome": 8, "Firefox": 23},
        os_counts={"Windows": 5, "Mac": 12}
    )
    db.session.add(record)
    db.session.commit()

    record = ArticleAnalytics(
        article_id='2',
        clicks=34,
        time_spent=12.5,
        browser_counts={"Chrome": 8, "Firefox": 23},
        os_counts={"Windows": 5, "Mac": 12}
    )
    db.session.add(record)
    db.session.commit()

    record = ArticleAnalytics(
        article_id='3',
        clicks=34,
        time_spent=12.5,
        browser_counts={"Chrome": 8, "Firefox": 23},
        os_counts={"Windows": 5, "Mac": 12}
    )
    db.session.add(record)
    db.session.commit()

    record = ArticleAnalytics(
        article_id='4',
        clicks=34,
        time_spent=12.5,
        browser_counts={"Chrome": 8, "Firefox": 23},
        os_counts={"Windows": 5, "Mac": 12}
    )
    db.session.add(record)
    db.session.commit()
    return "Inserted!"

@main.route('/test-fetch')
def fetch_test():
    records = ArticleAnalytics.query.all()
    return jsonify([
        {
            "article_id": r.article_id,
            "clicks": r.clicks,
            "time_spent": r.time_spent,
            "browser_counts": r.browser_counts,
            "os_counts": r.os_counts
        }
        for r in records
    ])

@main.route('/delete/<article_id>', methods=['GET'])
def delete_article(article_id):
    article = ArticleAnalytics.query.filter_by(article_id=article_id).first()
    if article:
        db.session.delete(article)
        db.session.commit()
        return f"Article '{article_id}' deleted."
    return "Article not found."
