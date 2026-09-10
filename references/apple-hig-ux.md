# Apple Human Interface Guidelines as a UX layer

Updated: 2026-09-11

This reference turns current, public Apple design guidance into practical checks for UI generation. Use the principles broadly; use Apple-specific dimensions and component conventions only when the target platform or interaction method makes them relevant.

## Core principles

Apple's 2026 HIG design principles are Purpose, Agency, Flexibility, Simplicity, Craft, and Delight. They are decision tools rather than a visual style recipe. The HIG overview also emphasizes hierarchy, harmony, and consistency for Apple-platform interfaces.

Sources:

- https://developer.apple.com/design/human-interface-guidelines/design-principles
- https://developer.apple.com/design/human-interface-guidelines/
- https://developer.apple.com/videos/play/wwdc2026/250/

The practical test is: can a person immediately understand what matters, what they can interact with, what will happen, and how to recover? A visually sparse screen is not automatically simple; sometimes context, status, or a progress indicator makes the experience simpler to understand.

## Structure and navigation

Apple's design-foundations session frames app structure, navigation, content, and visual design as connected layers. Start with the person's task and information structure before decorating the surface. Familiar relationships between controls and content make features easier to discover and make the interface feel grounded.

Sources:

- https://developer.apple.com/videos/play/wwdc2025/359/
- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/navigation-and-search

Practical rules:

- Keep the primary content and primary action obvious.
- Put controls near what they modify when that relationship is local.
- Prefer familiar navigation patterns over novel gestures that people must learn.
- Preserve location and state across transitions when possible so navigation feels continuous.
- Adapt layouts instead of merely shrinking them when space or text size changes.

## Feedback and recovery

Apple describes feedback as the way people learn current status, available next steps, the result of an action, and how to avoid or correct mistakes. Match the intensity of feedback to the importance of the event: passive status can stay inline, while potential data loss deserves stronger interruption.

Source:

- https://developer.apple.com/design/human-interface-guidelines/feedback

Practical rules:

- A tap or click should never feel ignored. Show pressed, selected, loading, progress, success, failure, or blocked state as appropriate.
- Keep routine status near the affected content instead of forcing a modal interruption.
- Offer undo or another recovery path for reversible actions when practical.
- Distinguish difficult-to-recover actions before commitment and explain the consequence in plain language.
- Do not rely on color, sound, or haptics alone to communicate important feedback.

## Controls, targets, and menus

Apple recommends comfortable control sizes and enough spacing to avoid accidental activation. The HIG accessibility guidance lists 44×44 pt as the default control size for iOS/iPadOS, and Apple's button guidance says custom buttons need a pressed state so people know their input was accepted.

Sources:

- https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://developer.apple.com/design/human-interface-guidelines/buttons
- https://developer.apple.com/design/tips/
- https://developer.apple.com/design/human-interface-guidelines/menus

Practical rules:

- On iOS/iPadOS, aim for at least 44×44 pt interactive targets for ordinary touch controls; do not blindly apply this number to every desktop control.
- Preserve adequate space between adjacent controls.
- Custom controls need visible hover/focus/pressed/selected/disabled states where the input method supports them.
- Prefer system or familiar control behavior when it already communicates the interaction well.
- In menus, place important/frequent actions early, group related commands, use clear action labels, and keep the menu short enough to scan.

## Typography and writing

Typography conveys both hierarchy and legibility. Apple recommends readable sizes, avoiding unnecessarily light weights, minimizing typeface variety, supporting Dynamic Type, and preserving information hierarchy as text grows. Apple treats interface writing as part of UX: vocabulary, tone, action labels, and multi-step terminology should be direct and consistent.

Sources:

- https://developer.apple.com/design/human-interface-guidelines/typography
- https://developer.apple.com/design/human-interface-guidelines/writing

Practical rules:

- Use a small number of type roles and make hierarchy obvious through size, weight, and color.
- Avoid layout assumptions that only work at one font size.
- Prefer action labels that describe the result: `Save`, `Retry`, `Remove`, `Continue`.
- Keep terminology stable across multi-step flows.
- Use placeholder text as a hint, not as the only label for information people may need after typing.

## Motion

Apple describes motion as a way to communicate status, feedback, instruction, and visual continuity. Motion should make state easier to understand. Accessibility guidance also calls for reducing automatic and repetitive motion when Reduce Motion is enabled, including excessive zooming, scaling, depth movement, and blur transitions.

Sources:

- https://developer.apple.com/design/human-interface-guidelines/motion
- https://developer.apple.com/design/human-interface-guidelines/accessibility
- https://developer.apple.com/videos/play/wwdc2018/803/

Practical rules:

- Animate cause and effect: reveal from the trigger, preserve spatial continuity, and let motion confirm state changes.
- Keep common transitions quick enough that they don't delay the task.
- Avoid bounce, large travel, depth motion, and blur animation when they add spectacle but no information.
- In reduced-motion mode, prefer simpler fades and state changes over translation/scale/depth effects.
- Capture interaction GIFs from the actual implementation so the preview reveals poor timing or confusing state changes.

## Accessibility is normal UX

Apple frames accessible interfaces as intuitive, perceivable, and adaptable. Accessibility improves the default experience too: larger hit targets, clear hierarchy, multiple feedback channels, predictable interactions, adaptable text, keyboard/focus support, and reduced motion all lower friction.

Source:

- https://developer.apple.com/design/human-interface-guidelines/accessibility

For each meaningful surface, check:

1. Can the task be completed using the expected input methods for the platform?
2. Does the interface remain understandable without relying on one sensory cue such as color or animation?
3. Does larger text preserve the task hierarchy and access to controls?
4. Are focus, labels, selection, and errors perceivable?
5. Does reduced motion preserve meaning and task completion?

## New Apple visual language

Apple's newer design-system material, including Liquid Glass, should be treated as a system of content hierarchy, adaptive structure, materials, and behavior rather than a blur preset. Use system materials and expressive visual effects only when they preserve readability, hit targets, hierarchy, and platform consistency.

Sources:

- https://developer.apple.com/videos/play/wwdc2025/356/
- https://developer.apple.com/videos/play/wwdc2025/219/

Do not add glass, translucency, concentric rounding, or floating controls merely to imitate Apple. The UX rules above have priority over the visual effect.
