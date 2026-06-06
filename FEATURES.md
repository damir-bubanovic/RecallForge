# RecallForge — Features Overview

## Goal

RecallForge is a desktop flashcard learning application focused on creating, organizing, and reviewing knowledge through a hierarchical structure of subjects, subfolders, and interactive question/answer cards.

Built using:

* Python
* PySide6
* SQLite

---

# Current Development Phase

RecallForge is currently in the foundation and architecture phase.

Current focus:

* Build a stable desktop application foundation
* Design the database architecture
* Implement subject management
* Implement subfolder management
* Implement card management
* Implement review mode
* Support images inside cards
* Keep the application fully offline and local-first

---

# Chapter 1: Desktop Application Foundation 🟡

## Planned

* Main application window
* Application navigation
* Window management
* Consistent UI styling
* Responsive desktop layout
* Reusable UI components

---

# Chapter 2: Subject Management 🔴

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

## Future Possibilities

* Subject icons
* Subject colors
* Subject statistics

---

# Chapter 3: Subfolder Management 🔴

## Purpose

Each subject can contain multiple subfolders.

Example:

History

* 18th Century
* French Revolution
* Egyptians
* Roman Empire
* World War I

Programming

* Python
* Java
* Databases
* Algorithms

## CRUD Features

### Create

* Create subfolder inside subject

### Read

* View all subfolders

### Update

* Rename subfolder

### Delete

* Delete subfolder

## Future Possibilities

* Nested subfolders
* Subfolder statistics
* Subfolder icons

---

# Chapter 4: Card Management 🔴

## Purpose

Cards are the core learning units of RecallForge.

Each card belongs to a specific subfolder.

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

## Future Possibilities

* Tags
* Difficulty levels
* Notes
* References
* External links

---

# Chapter 5: Review Mode 🔴

## Purpose

Review cards interactively.

## Review Flow

Question appears.

User clicks.

Answer appears.

User clicks again.

Next question appears.

User clicks.

Answer appears.

Continue until all cards have been reviewed.

## Planned Features

* One card at a time
* Question display
* Answer reveal
* Automatic progression
* End-of-session summary
* Restart review session

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

## Future Possibilities

* Multiple images per card
* Image zoom
* Drag-and-drop image support

---

# Chapter 7: SQLite Database 🔴

## Planned Tables

### Subjects

* id
* name
* created_at
* updated_at

### Subfolders

* id
* subject_id
* name
* created_at
* updated_at

### Cards

* id
* subfolder_id
* question_text
* answer_text
* question_image_path
* answer_image_path
* created_at
* updated_at

---

# Chapter 8: Search System 🔴

## Planned

Search through:

* Subjects
* Subfolders
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
* Total subfolders
* Total cards
* Cards reviewed
* Study sessions completed

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

# Chapter 13: UI / UX 🔴

## Planned

* Modern desktop interface
* Clean navigation
* Comfortable reading layout
* Dark mode support
* Light mode support

## Future Possibilities

* Custom themes
* Font size controls
* Accessibility improvements

---

# Architecture Overview

RecallForge Structure

Subject

└── Subfolder

    └── Card

        ├── Question

        ├── Question Image (Optional)

        ├── Answer

        └── Answer Image (Optional)

---

# Version 0.1 Scope

## Goals

1. Launch desktop application
2. Create SQLite database
3. Subject CRUD
4. Subfolder CRUD
5. Card CRUD
6. Review mode
7. Image support

---

# Recommended Development Order

## Phase 1

* Database schema
* Database helper functions

## Phase 2

* Subject management

## Phase 3

* Subfolder management

## Phase 4

* Card management

## Phase 5

* Review mode

## Phase 6

* Image support

## Phase 7

* Search system

## Phase 8

* Polish and optimization

---

# Summary

RecallForge is a local-first desktop learning application that organizes knowledge into subjects, subfolders, and interactive question/answer cards.

The initial goal is to create a complete offline flashcard system with image support, SQLite storage, and a clean PySide6 desktop experience.
