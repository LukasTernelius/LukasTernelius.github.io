---
layout: default
title: Projects
author: Lukas
nav: false
---

{% assign projects = site.posts | where: "category", "projects" | sort: "date" %}
## Projects

<ul>
  {% for post in projects %}
  <li>{{ post.date | date: "%Y-%m-%d" }} — <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

{% assign others = site.posts | where_exp: "post", "post.category != 'projects'" | sort: "date" %}
## Other posts

<ul>
  {% for post in others %}
  <li>{{ post.date | date: "%Y-%m-%d" }} — <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
