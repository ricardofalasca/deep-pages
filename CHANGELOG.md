# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html) since its version 0.1.1.

## [Unreleased]

## [0.1.7] - 2018-05-17
### Changed:
 - Fix: stupid error - forgot to import ObjectDoesNotExist (I'm shame about it)

## [0.1.6] - 2018-05-15
### Changed:
 - Fix: was a wrong code to detect and validate the page requested extension

## [0.1.5] - 2018-03-26
### Changed
 - Fix: there was a bug when we're using Middleware way and PageView was not configured.

## [0.1.4] - 2018-03-26
### Changed
 - Fix a stupid bug has been fixed after functions names refactoring
 - Fix images referenced in README.md

## [0.1.3] - 2018-03-26
### Added
 - Fix normalize_path() function to check if deeppages' path isn't the root path, otherwise change the requested path to compare with existent deep pages

## [0.1.2] - 2018-03-22
### Added
 - Refactor function get_page_by_path() in utils.py.
 - Add new function get_page_by_name() in utils.py.
 - Rename function render_template to render_content() in utils.py.
 - Add new function render_page() in utils.py.
 - Add new function render_requested_page_content() in utils.py.
 - Add new method render() on Page model returning a rendered template.
 - Add this CHANGELOG file based on keepachangelog.com.
 - Add new function is_acceptable_file_type() used for valid file type verification and avoid non-text-based content.

## [0.1.1] - 2018-03-21
### Changed
 - Add missing migration directory with initial migration (0001-initial.py) into dist package.

## [0.1] - 2018-03-21
### Added
 - First beta version published.
