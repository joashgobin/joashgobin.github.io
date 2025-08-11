# Mango CSS
This CSS project is based on CUBE CSS (https://cube.fyi) - a CSS methodology that prioritizes working with the strengths of CSS, not against them.

The project also uses SwupJS (https://swup.js.org) for page transitions and the CSS files cater for the transition states that SwupJS imposes on the HTML.

## Principles behind Mango CSS
- Font size and weigth are determined by the semantic HTML used e.g. **strong**, **h1**, **h2**, **p**, **small**, etc.
- Utils are used to layout elements on the page e.g. **.flex**. Utils are meant to do one job and do it well
- Tokens are the design tokens used to tweak the visuals of sub-sections of the HTML e.g. **.circle**, **.bp** (background primary), **.round** (round borders). Every design token is a util but tweaks only one thing
- Blocks are the boxed components that define a specific look e.g. **.card** and **.button** for an HTML element. Exceptions for each block are defined in the same CSS file as classes to be chained with the particular block e.g. **.card.no-pad** for a card with no padding