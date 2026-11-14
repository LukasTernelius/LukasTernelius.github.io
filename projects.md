---
layout: default
title: Projects
author: Lukas
nav: false
---

{% assign game_posts = site.posts | where: "category", "games" | sort: "date" | reverse %}
## Game projects

<ul>
  {% for post in game_posts %}
  <li>{{ post.date | date: "%Y-%m-%d" }} — <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

{% assign tech_posts = site.posts | where: "category", "tech" | sort: "date" | reverse %}
## Tech

<ul>
  {% for post in tech_posts %}
  <li>{{ post.date | date: "%Y-%m-%d" }} — <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
