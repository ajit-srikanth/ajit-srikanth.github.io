import re

with open("_layouts/default.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract everything between <main class="wrapper"> and </main>
match = re.search(r'(<main class="wrapper">\s*)(.*?)(\s*<!-- Footer -->)', content, re.DOTALL)
main_content = match.group(2)

# Create index.html
index_content = "---\nlayout: default\n---\n" + main_content

# Now replace the hardcoded publications with the dynamic loop
pub_loop = """      <!-- Publications -->
      <section class="section">
        <h2 class="sec-title" data-aos="fade-up"><span class="dot"></span>Publications</h2>
        <p class="pub-note" data-aos="fade-up" data-aos-delay="50">* denotes equal contribution &middot; click to expand</p>
        <div class="pub-list stagger">
          {% for post in site.posts %}
            {% if post.categories contains 'research' %}
            <div class="pub-card" data-aos="fade-up" data-aos-duration="400" data-aos-delay="50">
              <div class="pub-head" onclick="togglePub(this)">
                <div class="pub-info">
                  <div class="title">{{ post.title }}</div>
                  <div class="venue">{{ post.venue }}</div>
                </div>
                <div class="pub-pills">
                  {% if post.website %}<a href="{{ post.website }}" onclick="event.stopPropagation()"><i data-feather="globe" style="width:11px;height:11px;vertical-align:-1px;margin-right:2px;"></i>site</a>{% endif %}
                  {% if post.paper %}<a href="{{ post.paper }}" onclick="event.stopPropagation()"><i data-feather="file-text" style="width:11px;height:11px;vertical-align:-1px;margin-right:2px;"></i>paper</a>{% endif %}
                  {% if post.code %}<a href="{{ post.code }}" onclick="event.stopPropagation()"><i data-feather="github" style="width:11px;height:11px;vertical-align:-1px;margin-right:2px;"></i>code</a>{% endif %}
                  {% if post.video %}<a href="{{ post.video }}" onclick="event.stopPropagation()"><i data-feather="youtube" style="width:11px;height:11px;vertical-align:-1px;margin-right:2px;"></i>video</a>{% endif %}
                  {% if post.link %}<a href="{{ post.link }}" onclick="event.stopPropagation()"><i data-feather="link" style="width:11px;height:11px;vertical-align:-1px;margin-right:2px;"></i>link</a>{% endif %}
                </div>
                <div class="pub-arrow">▼</div>
              </div>
              <div class="pub-body">
                <div class="authors">{{ post.authors }}</div>
                <div class="abstract" style="margin-top:0.8rem; font-size:0.85rem; line-height:1.5; color:var(--text-secondary);">
                  {{ post.content }}
                </div>
              </div>
            </div>
            {% endif %}
          {% endfor %}
        </div>
      </section>"""

# Replace the publications section
index_content = re.sub(r'<!-- Publications -->.*?</section>', pub_loop, index_content, flags=re.DOTALL)

proj_loop = """      <!-- Projects -->
      <section class="section">
        <h2 class="sec-title" data-aos="fade-up"><span class="dot"></span>Projects</h2>
        <div class="proj-grid stagger">
          {% for post in site.posts %}
            {% unless post.categories contains 'research' %}
            <div class="proj-card" data-aos="fade-up" data-aos-duration="400">
              <img src="{{ site.baseurl }}/tn{{ post.image }}" alt="project image" class="proj-img" />
              <div class="proj-content">
                <h3>
                  {% if post.link %}
                    <a href="{{ post.link }}">{{ post.title }}</a>
                  {% else %}
                    {{ post.title }}
                  {% endif %}
                </h3>
                <div class="proj-links">
                  {% if post.website %}<a href="{{ post.website }}">site</a>{% endif %}
                  {% if post.paper %}<a href="{{ post.paper }}">paper</a>{% endif %}
                  {% if post.code %}<a href="{{ post.code }}">code</a>{% endif %}
                  {% if post.video %}<a href="{{ post.video }}">video</a>{% endif %}
                  {% if post.patent %}<a href="{{ post.patent }}">patent</a>{% endif %}
                </div>
                <div class="desc">{{ post.content | strip_html | truncatewords: 30 }}</div>
              </div>
            </div>
            {% endunless %}
          {% endfor %}
        </div>
      </section>"""

index_content = re.sub(r'<!-- Projects -->.*?</section>', proj_loop, index_content, count=1, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

# Update default.html
layout_content = content.replace(match.group(2), "\n    {{ content }}\n\n")
# remove layout: default from frontmatter
layout_content = re.sub(r'^---\nlayout: default\n---\n', '', layout_content)

with open("_layouts/default.html", "w", encoding="utf-8") as f:
    f.write(layout_content)
