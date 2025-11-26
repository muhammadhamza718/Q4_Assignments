# Project: Car Rental Website

## 1. Overview

This document outlines the specifications for a car rental website. The project will be a single-page static website built using HTML, CSS, and JavaScript, based on the provided Figma design.

## 2. Technology Stack

- **Structure:** HTML5
- **Styling:** CSS3
- **Language:** JavaScript (Vanilla)
- **Backend:** Static content (no backend required)

## 3. External Libraries

To support the core functionalities and styling requirements of the project, the following external libraries will be utilized:

- **Icon Library:**
  - Boxicons CDN - A simple and modern icon library.
- **Fonts:**
  - Google Fonts: 'Plus Jakarta Sans' and 'Inter' for typography.

## 4. Pages and Components

### 4.1. Main Page (`index.html`)

This will be the main entry point of the application and will contain the entire single-page layout. It will be composed of the following components:

### 4.2. Components (HTML Sections)

- **`Header`** (HTML `<header>` element):

  - Displays the company logo.
  - Contains a search bar with a filter icon.
  - Includes user action icons: "Likes," "Notifications," "Settings," and a "Profile" picture.

- **`Hero`** (HTML `<section>` element):

  - Displays two prominent promotional advertisements.
  - Each ad will have a title, a brief description, and a "Rental Car" button.

- **`Search`** (HTML `<section>` element with form):

  - A form for finding a rental car.
  - Contains "Pick-Up" and "Drop-Off" sections.
  - Each section has inputs for:
    - Location (dropdown).
    - Date (date picker).
    - Time (time picker).
  - A "Swap" button to interchange pick-up and drop-off details.

- **`CarCard`** (HTML `<div>` element):

  - Displays information for a single car.
  - Includes:
    - Car name and type (e.g., "Sport," "SUV").
    - "Like" (heart) button.
    - Car image.
    - Specifications: Fuel capacity, transmission type, seating capacity.
    - Price per day.
    - "Rent Now" button.

- **`CarList`** (HTML `<section>` element):

  - Organizes and displays multiple `CarCard` components.
  - Will have two main sections: "Popular Car" and "Recomendation Car".
  - Includes a "View All" link for the "Popular Car" section.
  - A "Show more car" button at the bottom to load more listings, showing the total number of available cars.

- **`Footer`** (HTML `<footer>` element):
  - Displays the company logo and a brief mission statement.
  - Contains navigation links organized into "About," "Community," and "Socials" sections.
  - Includes "Privacy & Policy" and "Terms & Condition" links.
  - A copyright notice.

## 5. Assets

All static assets like images and icons will be stored in the `public` directory.
