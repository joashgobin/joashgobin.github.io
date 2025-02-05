# Approach to Design

## Style reset
- Set all default paddings and margins to 0

## Typography
- Body: line-height 1.5, font size 1.2rem, font-family geometric-humanist, text-underline-offset 3px, color #2d2d2d
- Headings: line height 1.3, font-family neo-grotesque

## Whitespace
- Use a lot of whitespace
- Let your design breathe!

## Chunks of text
- Large paragraphs should be accompanied by a heading to help with context

## Images
- Set default image max-width to 100%

## Grouping of Elements
- Place the actual information for a section within a div with a specific class in order to make styling easier
- Style according to class name
- Avoid using the > with base elements like h1, strong, p, etc.
- Use class names that identify elements by their function and target these via selectors
- Use cards to group related images and text
- Use contrasting section background colors to distinguishing between sections
- Add a small padding to the sections to create a consistent alignment

## Use of Margins
- Use margins to keep objects away from each other, e.g. when you have links in a div, the links with the 0 margin will not be spaced out from other elements

## Stylesheet Structure
- Place element selectors followed by class selectors
- Create mobile versions of styling for selectors first
- Place media queries for a selector right after the mobile styling of that selector

## Use of Linear Gradients, Background Images, Borders and Box Shadows
- Border radius of 0.5rem to 1rem is fine
- Use larger border radius for smaller objects