from flask import Blueprint, request, redirect, url_for, render_template

from app.services.search import search_topic_paginated

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('')
def search():
    query = request.args.get('q')
    page = request.args.get('page', 1, type=int)

    if not query or query.strip() == '':
        return redirect(url_for('main.home'))

    results = search_topic_paginated(query, page)
    return render_template("search/results.html", results=results, query=query)