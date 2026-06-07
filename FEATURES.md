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

* Import / Export system
* Statistics system
* Review history
* Spaced repetition engine
* UI polish and optimization
* Maintain a clean and scalable architecture

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
* Reusable widget architecture

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

## Future Enhancements

* True spaced repetition
* Review statistics
* Review history
* Learning intervals
* Due card scheduling

---

# Chapter 6: Image Support ✅

## Purpose

Allow visual learning.

## Supported Formats

* PNG
* JPG
* JPEG
* WEBP
* SVG

## Implemented

* Image selection in Card Dialog
* Local image storage
* SQLite image path persistence
* Card Preview image display
* Review Mode image display
* Reusable ImageViewer widget
* SVG support

## Future Possibilities

* Multiple images per card
* Image zoom
* Drag-and-drop image support
* Full-screen image viewer

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

## Implemented Features

* Automatic database creation
* Automatic schema creation
* Subject CRUD operations
* Topic CRUD operations
* Card CRUD operations
* Foreign key relationships
* SQLite persistence

---

# Chapter 8: Search System ✅

## Implemented

Search through:

* Subjects
* Topics
* Question text
* Answer text

## Features

* Real-time search
* Case-insensitive matching
* SQLite powered search
* Unified search results
* Topic navigation from search results

## Future Improvements

* Auto-open selected cards
* Search highlighting
* Advanced filters

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
* Search panel
* Subject and Topic management
* Card list panel
* Card preview panel
* Review dialog
* Context menu workflow
* ImageViewer widget
* SVG image rendering

## Planned

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

## Planned Features

* Again
* Hard
* Good
* Easy
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
    └── Card
        ├── Question
        ├── Question Image (Optional)
        ├── Answer
        └── Answer Image (Optional)

---

# Current Project Structure

RecallForge

├── app/
│   ├── cards/
│   ├── dialogs/
│   ├── hierarchy/
│   ├── preview/
│   ├── review/
│   ├── search/
│   ├── utils/
│   ├── widgets/
│   └── main_window.py
│
├── database/
│   ├── connection.py
│   ├── schema.py
│   ├── subjects.py
│   ├── topics.py
│   ├── cards.py
│   └── search.py
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
8. Image Support ✔
9. Search System ✔

## Remaining

10. Import / Export
11. Statistics
12. Spaced Repetition Engine

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

## Phase 7 ✅

* Image Support

## Phase 8 ✅

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

RecallForge currently supports full subject management, topic management, card management, image-enhanced flashcards, card previewing, topic-based review sessions, and integrated search functionality.

The next milestone is Import / Export, followed by Statistics and a full Spaced Repetition Engine inspired by Anki.
