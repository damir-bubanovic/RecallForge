# RecallForge — Features Overview

## Goal

RecallForge is a desktop flashcard learning application focused on creating, organizing, and reviewing knowledge through a hierarchical structure of subjects, topics, and interactive question/answer cards.

Built using:

* Python
* PySide6
* SQLite

---

# Current Development Phase

RecallForge is currently in the core functionality phase.

Current focus:

* Improve review mode
* Add image support
* Add card statistics
* Add import/export functionality
* Maintain a clean and scalable architecture
* Prepare for future spaced repetition features

---

# Chapter 1: Desktop Application Foundation ✅

## Implemented

* Main application window
* PySide6 desktop application setup
* Window management
* Modular project structure
* Reusable panel architecture
* Clean separation between UI and database layers
* Context menu based workflow

---

# Chapter 2: Subject Management ✅

## Purpose

Subjects represent the highest level of knowledge organization.

Examples:

* History
* Accounting
* Programming
* Languages
* Biology
* Geography

## CRUD Features

### Create

* Create new subject

### Read

* View all subjects

### Update

* Rename subject

### Delete

* Delete subject

## Implemented

* Subject CRUD
* Subject persistence through SQLite
* Subject validation
* Context menu actions

## Future Possibilities

* Subject icons
* Subject colors
* Subject statistics

---

# Chapter 3: Topic Management ✅

## Purpose

Each subject can contain multiple topics.

Example:

History

* French Revolution
* Egyptians
* Roman Empire
* World War I
* 18th Century

Programming

* Python
* Java
* Databases
* Algorithms

## CRUD Features

### Create

* Create topic inside subject

### Read

* View all topics

### Update

* Rename topic

### Delete

* Delete topic

## Implemented

* Topic CRUD
* Topic hierarchy
* Topic persistence through SQLite
* Context menu actions

## Future Possibilities

* Nested topics
* Topic statistics
* Topic icons

---

# Chapter 4: Card Management ✅

## Purpose

Cards are the core learning units of RecallForge.

Each card belongs to a specific topic.

## Card Structure

### Question

* Question text
* Optional question image

### Answer

* Answer text
* Optional answer image

## CRUD Features

### Create

* Create card

### Read

* View cards

### Update

* Edit card

### Delete

* Delete card

## Implemented

* Card CRUD
* Reusable CardDialog
* Card list panel
* Card preview panel
* Context menu actions

## Future Possibilities

* Tags
* Difficulty levels
* Notes
* References
* External links

---

# Chapter 5: Review Mode ✅

## Purpose

Review cards interactively.

## Current Review Flow

Question appears.

User clicks **Show Answer**.

Answer appears.

User chooses:

* Again
* Hard
* Good
* Easy

Next question appears.

Continue until all cards have been reviewed.

## Implemented Features

* One card at a time
* Question display
* Answer reveal
* Topic-based review sessions
* Review completion message
* Anki-style rating buttons

## Current Rating Behavior

### Again

* Card is added back into the current review session

### Hard

* Move to next card

### Good

* Move to next card

### Easy

* Move to next card

## Planned Future Enhancements

* True spaced repetition
* Review statistics
* Review history
* Learning intervals
* Due card scheduling

---

# Chapter 6: Image Support 🔴

## Purpose

Allow visual learning.

## Supported Locations

### Question Side

* Image support

### Answer Side

* Image support

## Supported Formats

* PNG
* JPG
* JPEG
* WEBP

## Storage Strategy

Images stored locally.

Database stores image file paths only.

## Planned Integration

* Card Dialog
* Card Preview
* Review Mode

## Future Possibilities

* Multiple images per card
* Image zoom
* Drag-and-drop image support

---

# Chapter 7: SQLite Database ✅

## Implemented Tables

### Subjects

* id
* name
* created_at
* updated_at

### Topics

* id
* subject_id
* name
* created_at
* updated_at

### Cards

* id
* topic_id
* question_text
* answer_text
* question_image_path
* answer_image_path
* created_at
* updated_at

## Implemented Database Layer

* connection.py
* schema.py
* subjects.py
* topics.py
* cards.py

## Implemented Features

* Automatic database creation
* Automatic schema creation
* Subject CRUD operations
* Topic CRUD operations
* Card CRUD operations
* Foreign key relationships
* SQLite persistence

---

# Chapter 8: Search System 🔴

## Planned

Search through:

* Subjects
* Topics
* Questions
* Answers

## Features

* Real-time search
* Case-insensitive matching
* Fast SQLite search

---

# Chapter 9: Import & Export 🟡

## Planned

### Export

* JSON export
* Backup export

### Import

* JSON import
* Backup restore

## Purpose

Allow users to back up and transfer knowledge collections.

---

# Chapter 10: Statistics System 🟡

## Planned

### Statistics

* Total subjects
* Total topics
* Total cards
* Cards reviewed
* Study sessions completed
* Learning progress
* Review history

---

# Chapter 11: Local-First Philosophy ✅

RecallForge is designed to be:

* Fully offline
* Local-only
* Private
* User-controlled

## No Requirements For

* Accounts
* Internet connection
* Cloud services
* Subscriptions

---

# Chapter 12: Data Safety 🟡

## Planned

* Automatic backups
* Safe database operations
* Confirmation dialogs before deletion
* Recovery options

---

# Chapter 13: UI / UX 🟡

## Implemented

* Main desktop window
* Hierarchy tree panel
* Subject and Topic management
* Card list panel
* Card preview panel
* Review dialog
* Context menu workflow

## Planned

* Image display support
* Modern desktop styling
* Improved navigation
* Comfortable reading layout
* Dark mode support
* Light mode support

## Future Possibilities

* Custom themes
* Font size controls
* Accessibility improvements

---

# Chapter 14: Spaced Repetition System 🔴

## Purpose

Implement a learning system inspired by Anki.

## Planned Rating System

### Again

* Failed recall
* Review again soon

### Hard

* Difficult recall
* Short review interval

### Good

* Normal recall
* Standard review interval

### Easy

* Instant recall
* Long review interval

## Planned Features

* Review intervals
* Due cards
* Learning stages
* Ease factor
* Review history
* Scheduling engine

---

# Architecture Overview

RecallForge Structure

Subject

└── Topic

```
└── Card

    ├── Question

    ├── Question Image (Optional)

    ├── Answer

    └── Answer Image (Optional)
```

---

# Current Project Structure

RecallForge

├── app/

│   ├── dialogs/

│   │   └── card_dialog.py

│   │

│   ├── hierarchy/

│   │   ├── hierarchy_panel.py

│   │   ├── hierarchy_loader.py

│   │   ├── hierarchy_menu.py

│   │   └── hierarchy_actions.py

│   │

│   ├── cards/

│   │   ├── card_panel.py

│   │   ├── card_loader.py

│   │   ├── card_menu.py

│   │   └── card_actions.py

│   │

│   ├── preview/

│   │   └── card_preview.py

│   │

│   ├── review/

│   │   └── review_dialog.py

│   │

│   └── main_window.py

│

├── database/

│   ├── connection.py

│   ├── schema.py

│   ├── subjects.py

│   ├── topics.py

│   └── cards.py

│

├── data/

├── assets/

├── tests/

│

├── main.py

├── FEATURES.md

├── README.md

└── requirements.txt

---

# Version 0.1 Scope

## Completed

1. Launch desktop application ✔
2. Create SQLite database ✔
3. Subject CRUD ✔
4. Topic CRUD ✔
5. Card CRUD ✔
6. Card Preview ✔
7. Review Mode ✔

## Remaining

8. Image support
9. Search
10. Import/Export
11. Statistics

---

# Recommended Development Order

## Phase 1 ✅

* Database schema
* Database helper functions

## Phase 2 ✅

* Subject CRUD

## Phase 3 ✅

* Topic CRUD

## Phase 4 ✅

* Card CRUD

## Phase 5 ✅

* Card Preview

## Phase 6 ✅

* Review Mode

## Phase 7

* Image Support

## Phase 8

* Search System

## Phase 9

* Import / Export

## Phase 10

* Statistics

## Phase 11

* Spaced Repetition Engine

## Phase 12

* Polish and optimization

---

# Summary

RecallForge is a local-first desktop learning application that organizes knowledge into subjects, topics, and interactive question/answer cards.

The application currently supports full subject, topic, and card management, card previewing, and topic-based review sessions with Anki-style rating buttons.

The next milestone is image support, followed by search, import/export, statistics, and a true spaced repetition engine.
