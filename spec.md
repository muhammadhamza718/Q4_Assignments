# Canva Redesign Specification

## Overall Layout
- **Resolution:** ~1753 × 768 px (approx)
- **Structure:**
  - Top Navigation Bar — fixed, full width
  - Hero Section — centered headline + subtext + two buttons
  - Background: vertical gradient
    - #992bff (top) → #5a32fa (40%) → #13a3b5 (70%) → #93e8f6 (100%)
    - Smooth transition: deep purple → purple → teal → light cyan
- **Body font:** 'Canva Sans', 'Noto Sans Variable', 'Segoe UI', Helvetica, Arial, sans-serif
- **Fallback styling:** min-height: 100vh, overflow-x: hidden

## Top Navigation Bar
- **Height:** 80px
- **Padding:** 32px left/right, 20px top/bottom
- **Position:** fixed, top: 0, full width, z-index: 1000

### Left Side (Logo)
- **Text:** Canva
- **Font-family:** 'Canva Sans Display', cursive (italic-like)
- **Font-size:** 28px
- **Font-weight:** 600
- **Color:** #ffffff
- **Font-style:** italic

### Center Menu (navbar-center)
- **Menu items:** Design, Product, Plans, Business, Education, Help
- **Font-family:** 'Canva Sans', 'Noto Sans Variable', 'Segoe UI', Helvetica, Arial, sans-serif
- **Font-size:** 16px
- **Font-weight:** 500
- **Color:** #ffffff
- **Hover:** rgba(255,255,255,0.85)

### Right Side Buttons (navbar-right)
#### Sign up (btn-signup)
- **Background:** rgba(255,255,255,0.2)
- **Text color:** #ffffff
- **Font-weight:** 500
- **Padding:** 8px 16px
- **Border-radius:** 8px
- **Hover:** #8120e0

#### Log in (btn-login)
- **Background:** #ffffff
- **Text color:** #5a32fa
- **Font-weight:** 500
- **Padding:** 8px 16px
- **Border-radius:** 8px
- **Margin-left:** 8px

## Hero Section
- **Container (.hero-section):**
  - Flexbox: column, centered horizontally + vertically
  - Min-height: 100vh
  - Text-align: center
  - Position: relative
  - Overflow: hidden

### Hero Content (.hero-content)
- **Max-width:** 1000px
- **Margin:** auto
- **z-index:** 1

### Headline (.headline)
- **Text:** A new era <br> of imagination
- **Font-family:** 'Merriweather', serif
- **Font-weight:** 500
- **Font-size:** 90px (responsive)
- **Line-height:** 1.1
- **Color:** #ffffff
- **Font-variation-settings:** "opsz" 100
- **Margin-bottom:** 20px

### Subheadline (.subheadline)
- **Text:** Discover a whole new world of skills and tools designed to put your imagination to work.
- **Font-family:** 'Merriweather', serif
- **Font-weight:** 400
- **Font-size:** 24px
- **Line-height:** 1.5
- **Color:** #ffffff
- **Horizontal padding:** 20px

## Hero Buttons (.hero-buttons)
- **Container:** flex row, centered, gap: 16px, margin-top: 32px
- **Responsive:** switches to column on screens <768px

### Start designing for free (btn-primary)
- **Background:** rgba(255,255,255,0.94)
- **Text color:** #0f172a
- **Font-weight:** 600
- **Font-size:** 18px
- **Border-radius:** 8px
- **Padding:** 24px 24px

### Explore our launches (btn-secondary)
- **Background:** rgba(27,35,49,0.6)
- **Text color:** #ffffff
- **Font-weight:** 600
- **Font-size:** 18px
- **Border-radius:** 8px
- **Padding:** 24px 24px

## Responsive Design
- **≤1200px:** Headline 72px
- **≤992px:** Navbar-center hidden, Headline 60px, Subheadline 20px
- **≤768px:** Navbar padding reduced, Logo 24px, Buttons 6px 12px font-size 14px, Headline 48px, Subheadline 18px, Hero buttons stacked width 80%
- **≤576px:** Navbar wraps, Logo + buttons centered, Headline 36px, Subheadline 16px, Log in margin adjustments

## Visual Hierarchy
1. Background gradient (purple → cyan) draws focus downward
2. Headline: largest text, white, central focus
3. Subheadline: smaller white text, contextual information
4. Hero buttons: clear CTA, contrasting white and dark styles
5. Navbar: fixed, minimal intrusion, accessible navigation

