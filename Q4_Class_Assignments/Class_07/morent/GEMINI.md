# GEMINI.md - Project Context & Instructions

This file serves as the central source of truth for the Car Rental Website project. It aggregates key information from the project planning documents and provides clear instructions for development.

## 1. Project Overview

**Project:** Car Rental Website
**Goal:** Build a modern, responsive single-page website for renting cars, based on a Figma design. The website will be static.

**Figma Design:** [Link to Figma Design](https://www.figma.com/design/kpnZRtOyOFKExeU5UZ1pfy/Car-Rent-Website-Design---Pickolab-Studio--Community---Copy---Copy-?node-id=44-14919&t=jhCfW6yddNzd3y2M-4)

## 2. Technology Stack

-   **Structure:** HTML5
-   **Language:** JavaScript
-   **Styling:** CSS3

## 3. Architecture & Structure

The project follows a standard static website structure.

**Directory Structure:**

-   `/index.html`: The main HTML file.
-   `/css`: Contains the `style.css` file for all styling.
-   `/js`: Contains the `script.js` file for interactivity.
-   `/images`: Static image assets.
-   `/assets`: Other static assets like fonts.

**Data Flow:**

1.  All content (Cars, Locations, etc.) is hardcoded directly into the `index.html` file.
2.  The page is rendered statically by the browser.
3.  JavaScript in `script.js` handles user interactions like form input.

## 4. Data Structure

Detailed data structures for static content are located in `DATA.md`.

-   **Car**: Name, Type, Image, Fuel Capacity, Transmission, Seating Capacity, Price.
-   **Location**: Name.

## 5. Development Phases

Refer to `PLANNING.md` and `TASKS.md` for the detailed roadmap.

1.  **Setup:** Create the basic file structure (`index.html`, `css/`, `js/`).
2.  **HTML Structure:** Build the semantic HTML structure based on the Figma design.
3.  **Styling:** Apply CSS to match the design.
4.  **Interactivity:** Add JavaScript for any dynamic features.
5.  **Testing & Deployment:** Verify and deploy the static files to a web host.