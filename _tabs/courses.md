---
layout: page
title: Courses
icon: fas fa-graduation-cap
order: 1
---

An index of the undergraduate courses I have written up here. Each entry links
to that course's archive, where its posts are collected.

{%- comment -%}
  The `size` filter returns 0 for both nil (every entry commented out) and an
  empty list, so this guard holds however the registry is emptied.
{%- endcomment -%}
{% assign course_count = site.data.courses | size %}

{% if course_count == 0 %}

> No courses in the registry yet. Add entries to `_data/courses.yml`{: .filepath }
> and they will appear here.
{: .prompt-tip }

{% else %}

{% assign terms = site.data.courses | group_by: "term" %}
{% for term in terms %}

## {{ term.name }}

<ul class="course-list">
{% for course in term.items %}
  {% assign posts = nil %}
  {% assign course_url = nil %}
  {% if course.category %}
    {% assign posts = site.categories[course.category] %}
    {% assign cat_slug = course.category | slugify %}
    {% capture course_url %}/categories/{{ cat_slug }}/{% endcapture %}
  {% endif %}
  <li class="course-item">
    <div class="course-head">
      {% if course.code %}<span class="course-code">{{ course.code }}</span>{% endif %}
      <span class="course-title">
        {% if course.category %}
          <a href="{{ course_url | relative_url }}">{{ course.title }}</a>
        {% else %}
          {{ course.title }}
        {% endif %}
      </span>
    </div>
    <div class="course-meta">
      {% if course.subject %}<span>{{ course.subject }}</span>{% endif %}
      {% if course.instructor %}<span>{{ course.instructor }}</span>{% endif %}
      {% if posts %}
        <span>{{ posts.size }} post{% unless posts.size == 1 %}s{% endunless %}</span>
      {% else %}
        <span class="course-pending">write-up pending</span>
      {% endif %}
    </div>
    {% if course.summary %}<p class="course-summary">{{ course.summary }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

{% endfor %}

{% endif %}

<style>
  .course-list {
    list-style: none;
    padding: 0;
    margin: 0 0 1.5rem;
  }

  .course-item {
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.75rem;
    border: 1px solid var(--card-border-color, rgba(128, 128, 128, 0.3));
    border-radius: 0.5rem;
    background: var(--card-bg, transparent);
  }

  .course-head {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.5rem;
  }

  .course-code {
    font-family: var(--bs-font-monospace, monospace);
    font-size: 0.8rem;
    padding: 0.1rem 0.4rem;
    border-radius: 0.25rem;
    color: var(--text-muted-color, #6b7280);
    border: 1px solid var(--card-border-color, rgba(128, 128, 128, 0.3));
  }

  .course-title {
    font-size: 1.05rem;
    font-weight: 600;
  }

  .course-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 0.9rem;
    margin-top: 0.35rem;
    font-size: 0.82rem;
    color: var(--text-muted-color, #6b7280);
  }

  .course-pending {
    font-style: italic;
  }

  .course-summary {
    margin: 0.6rem 0 0;
    font-size: 0.92rem;
  }
</style>
