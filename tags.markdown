---
layout: page
permalink: /tags/
---

{% capture tags %}
  {% for tag in site.tags %}{{ tag[0] }}{% unless forloop.last %} {% endunless %}{% endfor %}
{% endcapture %}
{% assign sortedtags = tags | split: " " | sort %}

{% for tag in sortedtags %}
  <h3 id="{{ tag }}">{{ tag | replace: "-"," " }}</h3>
  <ul>
  {% for post in site.posts %}
    {% if post.tags contains tag %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
  </ul>
{% endfor %}
