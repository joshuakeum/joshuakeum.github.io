# Print a post's body as HTML, rendered by kramdown the way Jekyll renders it here.
# Usage: bundle exec ruby render.rb POST.md   (seed.py reads the output)
require "kramdown"
require "kramdown-parser-gfm"

body = File.read(ARGV.fetch(0), encoding: "UTF-8").sub(/\A---\n.*?\n---\n/m, "")
print Kramdown::Document.new(body, input: "GFM", auto_ids: true, hard_wrap: false).to_html
