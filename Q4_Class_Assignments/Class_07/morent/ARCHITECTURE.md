# Car Rental Website - System Architecture

This document provides a detailed overview of the system architecture for the car rental website. It outlines the project structure, component hierarchy, and data flow.

## 1. Architectural Overview

The application will be a static website built using **HTML5** and styled with **CSS3**. Interactivity will be handled by **vanilla JavaScript**. This approach ensures a lightweight, performant, and easily deployable website.

-   **Structure:** HTML5
-   **Styling:** CSS3
-   **Interactivity:** JavaScript

Key architectural principles include:
-   **Static First:** The entire website will be a single `index.html` file, making it fast and easy to serve.
-   **Separation of Concerns:** The project structure is organized to clearly separate HTML structure, CSS styles, and JavaScript logic.
-   **Semantic HTML:** The markup will use semantic HTML5 tags for better accessibility and SEO.

## 2. Detailed Project Structure

The project will follow a standard static website structure.

```
/
|-- index.html              # The main and only HTML file
|-- css/
|   |-- style.css           # All CSS styles for the project
|-- js/
|   |-- script.js           # JavaScript for interactivity
|-- assets/                 # For other assets like fonts
|   |-- fonts/
|-- images/                 # For all images used in the project
|   |-- cars/
|   |-- icons/
|-- README.md
```

### Directory Explanations:

-   **`index.html`**: The root file containing the entire HTML structure of the page.
-   **`css/style.css`**: This file will contain all the CSS rules to style the website according to the Figma design.
-   **`js/script.js`**: This file will handle any dynamic behavior, such as form interactions or toggling UI elements.
-   **`assets/` and `images/`**: These directories will store all static assets required by the project.

## 3. Component Architecture

The `index.html` file will be structured into semantic sections that represent the different "components" of the page.

-   **`<header>`**: Will contain the logo, navigation, and user-related icons.
-   **`<main>`**: Will be the primary container for the page content.
    -   **`<section id="hero">`**: The hero section with promotional content.
    -   **`<section id="search">`**: The car rental search form.
    -   **`<section id="car-list">`**: The section displaying popular and recommended cars.
-   **`<footer>`**: The footer containing links, company info, and legal notices.

## 4. Data Flow

All data for the website, such as car listings and promotional text, will be **statically hardcoded** directly into the `index.html` file. There will be no external database or API calls.

## 5. State Management

Any required state, such as the values in the search form, will be managed locally within the browser using **vanilla JavaScript**.

## 6. Styling

-   **CSS3:** All styling will be done using standard CSS.
-   **`style.css`**: A single stylesheet will contain all the styling rules, organized by section.
-   **BEM (Block, Element, Modifier):** A naming convention like BEM might be used to keep the CSS organized and maintainable.