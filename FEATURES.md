# RecallForge — Features Overview

## Goal

RecallForge is a desktop flashcard learning application focused on creating, organizing, and reviewing knowledge through a hierarchical structure of subjects, topics, and interactive question/answer cards.

Built using:

* Python
* PySide6
* SQLite

---

# Current Development Phase

RecallForge is currently in the release preparation phase.

Current focus:

* UI polish
* Architecture cleanup
* User experience improvements
* Data safety improvements
* Release readiness
* Documentation

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
* Theme management system
* Persistent application settings

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
* Topic icons

---
# Chapter 4: Card Management ✅

## Purpose

Cards are the core learning units of RecallForge.

Each card belongs to a specific topic.

## Card Structure

### Question

Rich content supporting:

* Text
* Bold formatting
* Italic formatting
* Underline formatting
* Font size controls
* Bullet lists
* Numbered lists
* Embedded images

### Answer

Rich content supporting:

* Text
* Bold formatting
* Italic formatting
* Underline formatting
* Font size controls
* Bullet lists
* Numbered lists
* Embedded images

## Implemented

* Card CRUD
* Reusable CardDialog
* Rich text editor
* Embedded image support
* Card list panel
* Card preview panel
* Context menu actions
* HTML content rendering
* Rich text persistence

## Future Possibilities

* Tags
* Difficulty levels
* Notes
* References
* External links
* Text highlighting
* Code blocks
* Drag-and-drop images
* Clipboard image paste

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
* Review history logging
* Learning strength tracking

## Current Rating Behavior

### Again

* Review is logged
* Card is added back into the current review session

### Hard

* Review is logged
* Learning strength updated
* Move to next card

### Good

* Review is logged
* Learning strength updated
* Move to next card

### Easy

* Review is logged
* Learning strength updated
* Move to next card

## Integrated Systems

* Review History
* Learning Engine
* Statistics System

---
# Chapter 6: Embedded Image Support ✅

## Purpose

Allow visual learning directly inside card content.

## Supported Formats

* PNG
* JPG
* JPEG
* WEBP
* SVG

## Implemented

* Embedded images inside questions
* Embedded images inside answers
* Local image storage
* Rich text and image integration
* Image rendering in Card Preview
* Image rendering in Review Mode
* SVG support
* Automatic image scaling
* High-quality image rendering

## Benefits

* Images stay attached to content
* No separate image fields
* Cleaner card structure
* Richer learning material
* More flexible note creation

## Future Possibilities

* Drag-and-drop images
* Clipboard image paste
* Multiple image layouts
* Image resizing controls
* Image alignment controls
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
* created_at
* updated_at


### Review History

* id
* card_id
* rating
* reviewed_at

## Implemented Features

* Automatic database creation
* Automatic schema creation
* Subject CRUD operations
* Topic CRUD operations
* Card CRUD operations
* Review history persistence
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

# Chapter 9: Import & Export ✅

## Implemented

### Export

* JSON export
* Backup export

### Import

* JSON import
* Backup restore
* Import validation
* Import safety confirmation dialog

## Purpose

Allow users to back up and transfer knowledge collections.

## Features

* Preserves subjects
* Preserves topics
* Preserves cards
* Preserves card metadata
* Safe data replacement workflow

---

# Chapter 10: Statistics System ✅

## Purpose

Provide insight into collection growth and learning activity.

## Collection Statistics

* Total subjects
* Total topics
* Total cards


## Organization Statistics

* Average cards per topic
* Largest topic card count
* Top topics by card count
* Top subjects by card count

## Review Statistics

* Total reviews
* Reviews today
* Reviews this week
* Again review count
* Hard review count
* Good review count
* Easy review count

## Learning Statistics

* New cards
* Weak cards
* Familiar cards
* Strong cards

## Implemented Features

* Scrollable statistics dialog
* Reusable statistics sections
* Collection analytics
* Review analytics
* Learning analytics

---

# Chapter 11: Local-First Philosophy ✅

RecallForge is designed to be:

* Fully offline
* Local-only
* Private
* User-controlled

## Benefits

* No cloud dependency
* No account required
* No subscriptions
* No internet connection required
* Full ownership of learning data

---

# Chapter 12: Data Safety 🟡

## Implemented

* Import validation
* Import safety confirmation dialog
* SQLite foreign key protection
* Local data ownership

## Planned

* Automatic backups
* Safe database snapshots
* Recovery options
* Backup manager

---

# Chapter 13: UI / UX ✅

## Implemented

### Core Interface

* Main desktop window
* Hierarchy tree panel
* Search panel
* Card list panel
* Card preview panel
* Review dialog
* Statistics dialog

### User Experience

* Context menu workflow
* Reusable widget architecture
* Scrollable statistics window
* Cleaner panel organization
* Reusable statistics sections

### Rich Text Editor

Implemented

* Bold formatting
* Italic formatting
* Underline formatting
* Font size controls
* Bullet lists
* Numbered lists
* Embedded images
* HTML content rendering
* Rich text preview
* Rich text review mode


### Appearance

* Application branding
* SVG application logo
* Custom application icon
* Dark mode
* Light mode
* Persistent theme settings
* Automatic theme restoration on startup

### Visual Components

* SVG image rendering
* ImageViewer widget
* StatisticsSection widget

## Future Possibilities

* Custom themes
* Font size controls
* Accessibility improvements
* Optional layout customization

---

# Chapter 14: Learning Engine ✅

## Purpose

Create a pressure-free learning system built around review history and learning analytics.

## Implemented Features

### Review Tracking

* Review history logging
* Rating persistence
* Learning analytics foundation

### Learning Strength Classification

Cards are automatically categorized as:

* New
* Weak
* Familiar
* Strong

### Analytics Integration

* Statistics integration
* Learning strength reporting
* Collection insight generation

## Explicitly Not Required

RecallForge intentionally avoids:

* Due dates
* Overdue cards
* Daily quotas
* Forced study schedules
* Punishment-based learning systems

## Design Philosophy

Users should learn at their own pace.

The system provides insight and feedback rather than deadlines and pressure.

---

# Architecture Overview

RecallForge Structure

Subject
└── Topic
└── Card
├── Rich Question Content
│   ├── Text
│   ├── Formatting
│   ├── Lists
│   └── Embedded Images
│
└── Rich Answer Content
├── Text
├── Formatting
├── Lists
└── Embedded Images

```
    ↓
```

Review History
↓

Learning Engine
↓

Statistics System


---

# Architecture Principles

RecallForge follows a simple layered architecture:

## Presentation Layer

Responsible for:

* Windows
* Dialogs
* Panels
* Widgets
* User interactions

Examples:

* MainWindow
* CardDialog
* ReviewDialog
* StatisticsDialog
* StatisticsSection
* ImageViewer

## Action Layer

Responsible for:

* User-triggered operations
* UI-to-database coordination
* Error handling

Examples:

* card_actions.py
* hierarchy_actions.py

## Persistence Layer

Responsible for:

* SQLite operations
* CRUD logic
* Statistics queries
* Learning analytics
* Import / Export operations

Examples:

* subjects.py
* topics.py
* cards.py
* reviews.py
* statistics.py
* learning.py

---

# Current Project Structure

RecallForge

├── app/
│   ├── cards/
│   ├── dialogs/
│   ├── hierarchy/
│   ├── import_export/
│   ├── preview/
│   ├── review/
│   ├── search/
│   ├── statistics/
│   ├── theme/
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
│   ├── reviews.py
│   ├── learning.py
│   ├── search.py
│   ├── statistics.py
│   ├── import_data.py
│   └── export_data.py
│
├── assets/
│   └── logo.svg
│
├── data/
├── tests/
│
├── main.py
├── FEATURES.md
├── README.md
└── requirements.txt

---

# Version 0.1 Scope

## Completed

1. Desktop Application Foundation ✔
2. SQLite Database ✔
3. Subject CRUD ✔
4. Topic CRUD ✔
5. Card CRUD ✔
6. Card Preview ✔
7. Review Mode ✔
8. Image Support ✔
9. Search System ✔
10. Import / Export ✔
11. Statistics System ✔
12. Review History ✔
13. Learning Engine ✔
14. Dark Mode ✔
15. Theme Persistence ✔
16. Application Branding ✔
17. Rich Text Editor ✔
18. Embedded Images ✔


## Remaining

* UI polish
* Data safety improvements
* Documentation
* Release preparation

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

## Phase 9 ✅

* Import / Export

## Phase 10 ✅

* Statistics System

## Phase 11 ✅

* Review History

## Phase 12 ✅

* Learning Engine

## Phase 13 🟡

* UI polish
* Architecture cleanup
* Theme system
* Branding
* User experience improvements

## Phase 14

* Release preparation

---

# Current Status

RecallForge currently provides:

### Knowledge Management

* Subject management
* Topic management
* Card management
* Rich-text flashcards
* Embedded image support


### Learning

* Interactive review sessions
* Review history tracking
* Learning strength classification
* Learning analytics

### Productivity

* Real-time search
* Import / Export
* Statistics dashboard

### User Experience

* Dark mode
* Light mode
* Persistent theme settings
* Application branding
* SVG support

### Technical Foundation

* SQLite persistence
* Modular architecture
* Reusable widgets
* Local-first design
* Offline operation

---

# Summary

RecallForge is a fully offline desktop flashcard application focused on creating, organizing, reviewing, and analyzing knowledge through a simple hierarchy of subjects, topics, and cards.

The application now includes:

* Complete CRUD functionality
* Rich Text Editor
* Embedded Images
* Review Mode
* Review History
* Learning Engine
* Collection Statistics
* Learning Statistics
* Import /Export
* Dark Mode
* Persistent User Preferences
* Application Branding


RecallForge remains:

* Fully offline
* Local-first
* Private
* User-controlled
* Pressure-free

The current focus is final UI polish, documentation improvements, release preparation, and preparing the first stable public release.

---