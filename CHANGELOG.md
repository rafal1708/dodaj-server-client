# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.0] - 2024-10-05

### Added
- two config files, one for client and one for a server

### Changed
- now it works on local network (instead of localhost only) as a client-server
- switch from sqlite3 to mariadb



## [0.1.3] - 2024-09-12

### Added

- scraping games from gry-online website
- distinction between books and comic books
- links to categories
- API queries parameters: category (książka, komiks, gra komputerowa), and tag (search for a keyword in description and notes)

### Changed
- new logic; now main file will import module responsible for adding specific item (books, pc games etc.)


## [0.0.2] - 2024-08-30

### Changed
- link validation
- resolving host ip


## [0.0.1] - 2024-08-29

### Added

- first release
- automatically adding book to database