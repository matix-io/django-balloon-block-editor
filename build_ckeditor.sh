#!/bin/bash
(
  cd ckeditor5-build
  npm install
  npx webpack
)

cp ckeditor5-build/build/ckeditor.js balloon_block_editor/static/balloon_block_editor/ckeditor.js
cp ckeditor5-build/build/ckeditor.js.map balloon_block_editor/static/
