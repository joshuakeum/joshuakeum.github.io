---
title: Personal Projects
icon: fas fa-folder-open
order: 3
---

{%- comment -%}
  Lists every post in the "Personal Projects" category, newest first. To add a
  project, write a post with `categories: [Personal Projects]`; its
  `description` is shown under the title.
{%- endcomment -%}
{% assign projects = site.categories['Personal Projects'] %}

<ul class="project-list">
{% for project in projects %}
  <li class="project-item">
    <a class="project-title" href="{{ project.url | relative_url }}">{{ project.title }}</a>
    {% if project.description %}<p class="project-summary">{{ project.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

<style>
  .project-list {
    list-style: none;
    padding: 0;
    margin: 0 0 1.5rem;
  }

  .project-item {
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.75rem;
    border: 1px solid var(--card-border-color, rgba(128, 128, 128, 0.3));
    border-radius: 0.5rem;
    background: var(--card-bg, transparent);
  }

  .project-title {
    font-size: 1.05rem;
    font-weight: 600;
  }

  .project-summary {
    margin: 0.6rem 0 0;
    font-size: 0.92rem;
  }
</style>
