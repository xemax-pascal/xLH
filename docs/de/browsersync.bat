:: https://browsersync.io/#install
:: https://browsersync.io/docs/options/#option-notify
::C:\Users\PascalHelfenstein\AppData\Roaming\npm\node_modules\browser-sync\dist\default-config.js
:: npm install -g browser-sync

@echo off
cd /d %~dp0
cd site_de
dir
browser-sync start --server --no-notify --files "*.html"
