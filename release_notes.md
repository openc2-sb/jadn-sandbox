
# JADN Sandbox Release Notes

## 🚀 Release v0.18.0

This release improves schema transformation capabilities and makes schema validation errors easier to understand and resolve.

✨ What’s New

JADN 2.0 Support in Schema Transformation

Transformation Schema Resolver function now supports JADN 2.0.
One Base schema may reference multiple other JADN schemas, as long as their namespaces align
Enables more flexible and modular schema composition

🔍 Clearer Validation Errors

Improved error messages for schema inheritance validation
Errors are now more descriptive and user-friendly, helping to identify and fix issues faster

🧩 Why It Matters

Easier reuse of JADN Schemas across projects
Better feedback when working with complex schema hierarchies
Improved alignment with the latest JADN standard

## v0.17.0

Version 0.17.0 delivers a more stable, consistent, and user-friendly experience across the JADN Sandbox. This release focuses on improving data translation reliability, enhancing error feedback, strengthening validation alignment, and addressing several long-standing UX issues.

Additionally, going forward the project has formally moved to its new GitHub home under [openc2-sb](https://github.com/openc2-sb).

## Key Enhancements

* Resolved Redux state update issues when pasting schemas into the Data Translation panel, improving reliability and preventing unexpected UI behavior.
* Improved Compact, Concise, and Verbose data translation for consistent and predictable conversions across formats.
* Corrected root-selection logic during schema translation to ensure accurate processing of nested and complex schemas.
* Enhanced error messaging throughout the application, providing clearer, more actionable diagnostics for users.

## Known Issues

* XML Nil logic is not yet implemented, possibly causing issues with Optional fields.
* XML MapOf validation for XML data requires additional refinement.
* XML Array validation for IP-net formats remains incomplete.
* Schema transformation logic (combining multiple schemas) requires updates to align with JADN 2.0 updates.

## Conclusion

The 0.17.0 release strengthens the foundation of the JADN ecosystem through more dependable translation behavior, clearer user guidance, and improved alignment between the Sandbox and CLI. These updates, combined with the transition to the new GitHub organization, position the project for continued growth, expanded XML support, and deeper integration of JADN 2.0 capabilities.

## v0.16.0

This release deepens compatibility with **JADN 2.0**, strengthens data validation (especially around network and numeric formats), and introduces key UX improvements for navigating schema inheritance and binary data visualization. Together, these updates enhance both the flexibility and reliability of schema-based data workflows.

## Issue Fixes

### **Data & JADN Validation**

* Fixed XML and JSON wrappers requiring manual removal during validation.
* Corrected XML lists that appeared as dictionaries during parsing.
* Fixed regex validation errors for XML tags with prefixed namespace identifiers (`n:`).
* Improved IP network data validation — now supports **IPv4-net** and **IPv6-net** formats.
* Added support for **f128** and **f256** numeric formats.
* Updated integer format validation for JADN schemas.
* Added JSON-formatted IP-net validation for consistent format checking.

### **Schema Creation**

* Fixed `sbToastSuccess` notification bug during schema save operations.
* Resolved duplicate field ID issues when types inherit from extended fields.
* Updated logic to allow **Restrict** and **Extend** operations to overwrite inherited fields cleanly.
* Added support for **recursive inheritance**, ensuring complex types inherit all fields correctly across multiple layers.
* Updated JADN XML to use **Raw URL references** for base type schema locations.

### **JADN CLI / Validation**

* Updated schema validation API to use the new **JADN 2.0 validation standard**.
* Incorporated XSD attribute logic into CLI operations for improved schema accuracy.
* Rebuilt key reference schemas using **JADN 2.0**:

  * AP Hunt
  * OC2 v1.0.1
  * OC2 v1.1

## ⚙️ Essential Updates

### **Data Creation Enhancements**

* Added new “Combine Logic” operation for merging data creation behaviors.
* Improved IPv4Net and IPv6Net handling within data creation workflows.
* Completed final logic updates for data creation consistency and error handling.

## Enhancements

### **Usability & Visualization**

* Added **tooltips** in both **Schema Creation** and **Data Creation** views to visualize **inheritance hierarchies** for complex types.
* Added a **CBOR Annotated Hex View** in Data Creation for deeper binary-format inspection.
* Condensed and optimized Data Creation code for better performance and maintainability.

## v0.15.1

This release introduces **new data creation logic, alternative viewers (XML & CBOR), expanded validation**, and delivers several **schema creation fixes and UI improvements**.

## Highlights

* Added **Abstract / Restricts / Extends logic** and **recursive Key/Link handling**
* Introduced **XML & CBOR viewers** alongside JSON
* Implemented **Global Schema State via Redux**
* Fixed **schema creation bugs** (element count, empty array fields) and **syntax color scheme**

## Features

* **Data Creation**
  * Added **Abstract / Restricts / Extends logic** for flexible schema modeling
  * Added **Key/Link recursion handling** for recursive schema support
  * Introduced **Compound type options**
  * Added **Set** and **Unordered** option types
  * Introduced **XML & CBOR viewers** for alternative data representations
  * Added **highlighting** between input fields and JSON output
  * Implemented **Global Schema State via Redux** for consistent state management

* **Validation**
  * Expanded **string format options** in JADN validation

## Improvements

* **Schema Creation**
  * Redesigned **Option Modal** for better usability

* **Sandbox**
  * Reviewed & updated **Visualization Schema Loader**

## Fixes

* **Schema Creation**
  * Fixed **incorrect element count** bug
  * Fixed missing **empty array field** for `ArrayOf` and `MapOf`

* **Sandbox**
  * Corrected **syntax color scheme** in editor

## v0.15.0

### Major Features and Improvements

* Migrated Metaschema to a common repository.
* Rebuilt OSCAL SSP, POAM, AR, Profile, Component, Catalog, and AP using JADN 2.0.
* Aligned all major JADN Sandbox features (generation, translation, visualization, data creation, schema creation, validation) with JADN 2.0.
* Redesigned field options modal and rebuilt the data creation page.
* Created new data creation page and improved fullscreen data creator and JSON viewer.
* Added copy/duplicate type feature and set startup schema as the first example.
* Enabled quick navigation between schema and data creation.
* Improved CLI commands, setup GitHub CICD, and created customer CLI wheel.
* Created updated JADN2 wheel files.

### Schema and Data Creation

* Added features for unique/ordered, const, and default options in schema/data creation.
* Enhanced validation for arrays, maps, numbers, dates, and durations.
* Added string-based XML format and date/duration XML formats.
* Added JADN 2.0 decimal formats and primitives to ktype selection.
* Updated schema structure (exports to roots, imports to namespaces, info to meta).
* Improved handling of enumerated pointers, array/map logic, and input state.
* Improved input validation and dynamic form generation.
* Enhanced handling of nested structures and optional type headers.
* Added info button for comments and changed path to create/data.
* Improved data creation UI and usability, including enum pointer dropdown, field multiplicity, and calendar addon.
* Added save/load for data builder state and clear fields button.
* Improved handling for date/time, binary info viewer, and MapOf with enumerated key.
* Addressed issues with fields losing value, struct disappearance, and ID display.
* Addressed issues with ArrayOf & MapOf in data creation.
* Improved data creation for required data, date/time handling, and user prompts.
* Improved error handling and readability.
* Improved logic for required/optional fields and input validation.
* Improved handling of dynamic forms and JSON generation.

### Validation and Formats

* Incorporated XSD attribute logic and new JADN 2.0 string, integer, decimal, binary, and duration formats.
* Enhanced validation for binary options and inclusive/exclusive value limits.
* Enhanced validation logic: inheritance, choice in array, multiplicity, derived enumerations, and ID logic.
* Enhanced validation for signed/unsigned integers and schema logic.
* Added JADN CLI bulk converter.
* Added JADN 2.0 XML format validations and supporting code for new formats (string, decimal, duration, integer, binary).
* Updated supporting wheels and added XSD/XML validation tests.
* Applied updates for Music DB, OpenC2, and OSCAL Assessment Plan data validation.

### CLI and Automation

* Added and improved JADN CLI commands: direct commands, configurable prompts, schema conversion, validation, and reporting.
* Addressed critical dependency vulnerabilities.
* Added JIDL to JADN conversion and separated translations from visualizations.

### Other Improvements

* Improved logic for required/optional fields and input validation.
* Improved handling of dynamic forms and JSON generation.
* Improved error handling and readability.

## v0.14.0

* Schema and Data drop downs are now sorted in alphabetical order.
* Data Validation - Major update and overhaul of the Data Validation logic. Includes JSON, CBOR and XML improvements.
* Data Validation - Logic added to allow users to validate simple primitive data, as well as, complex structures.
* Data Validation - Adjustments to the logic to align with [JADN 2.0](https://docs.oasis-open.org/openc2/imjadn/v2.0/imjadn-v2.0.html>)
  * Further JADN 2.0 application updates coming soon

## v0.13.2

* Message Creation - The display of the Fixed IP-Net format option has been improved.
* Schema Creation - Enhanced the creation of IPv4 Net and IPv6 Net.
* Schema Creation: Within Fields, tabbing to the Field Deletion button comes after the comment input (last tabbable item within the field, rather than the first).
* Visualization - You now have more chart generation options, including Conceptual, Logical, and Informational.
* Translation - Resolved an Undefined Error that occurred when translating JSON to JADN. Additionally, "definitions" / "$defs" are no longer required for JSON to JADN translations.
* Schema Creation - Number Formatting logic has been enhanced.
* Data Validation - Pydantic handling of IP-Net formats has been improved.
* App Startup - The startup URL has been adjusted for better consistency.

## v0.13.1

* Data Creation - Date inputs allow past dates and times
* Data Generation - Performance improvements
* Schema Creation - UUID Binary format option added
* Translate - Allows .JIDL file extensions
* Validation improvements on certain format options
* Various Pages - Improved promise stability and drop down option wrapping
* Visualization - Utilizes the latest JADN lib enhancements for GraphViz and PlantUML Diagrams
* Visualization - Displaying enumerations and cardinality in GraphViz and PlantUML
* Visualization - Tightened white space on .JIDL files

## v0.13.0

* Data Generation - Improved performance and the ability to handle larger schemas
* Dependencies - Updated JADN from 0.6.23 to 0.7.4
* Translation - Introduced JIDL to JADN translation logic
* Translation and Generation - Improved MapOf converstion logic
* Transformation - Fixed random unwrapped results
* Transformation - Improved error response and general usage

## v0.12.1

* Schema Creation - Removed the UUID String Format (will be moved under Binary soon)

## v0.12.0

* Schema Creation - Added the UUID String Format
* Schema Creation - Added f64 Floating Point Precision for Numbers
* Schema Creation - Enhanced export logic to include checked vs. default
* Data Creation - Included validation logic for UUID
* Validation - Improved Export Naming Convention validation logic to allow for custom conventions via the Configuration Information
* Data Translation - Introduced the new Data Translation page which can translate valid JSON into CBOR Hex and CBOR Annotated Hex or XML

## v0.11.2

* Data Generation - Added a warning, if the user is missing Exports
* Data Creation - Minor input and button cleanup
* Data Creation - Several issues addressed
  * Regex input fields are now checked
  * Nested arrays display multiple entries correctly
  * Comments are being displayed correctly
  * Type checking logic refinement applied
  * Null values no longer incorrectly added to select fields

## v0.11.1

* Data Generation - Updated generation logic with Faker
* Data Generation - Improved string data consistency, removed outlier characters
* Data Generation - Multiple Choice options fixed
* Schema Creation - Improved validation of ECMAScript Regex
* Data Creation - Ability to check Schema Regex validity

## v0.11.0

* Data Validation - UUID Button added
* Data Validation - File upload only allows JADN
* Data Generation - XML/JSON Generation & Refinement

## v0.10.0

* Schema Creation - Ability to search through Outline based on type name
* Schema Creation - Ability to add Exports to schema Types
* Schema Creation - Restrict user from including regex and pattern Type Options together
* Schema Creation - Improved drag and drop feature
* Translation - Improved XSD Array and Map translations
* Data Creation - Added data handling for dir field option
* Data Creation - Integer fields do not allow characters: "e", "E", "+", "-"
* Data Creation Bug Fix - Boolean type check
* JADN Schema Validation - Updated validation to check for valid Exports, ktype, and vtype
* Code Reduction - use of const and common components
* Changed Conversion labeling and text to Visualization
* Added informative text to guide user when drop downs have no options

## v0.9.1

* Changed Message labeling and text to Data
* Improved json vs jadn schema loader
* Removes redundant json validation
* Updated JADN to XSD logic

## v0.9.0

* Translation - Initial implementation of JADN to XSD Translation
* Translation - Introduced JSON Schema to JADN Translation
* Schema Creation - Lazy loading tied to scrolling
* Schema Creation - Clear All Toast button
* Schema Creation - Enhanced Fields Drag and Drop capabilities
* Schema Creation - Updated Enum Field Options to a Drop Down of Types
* Improved file load error handling

## v0.8.0

* Removed react-strap and installed bootstrap 5.3.2
* Various UI updates across the app to enhance usability
* Added various Modal Confirmations for deletions and resets
* Schema Creation - Introduced a Scroll Highlight on the Outline
* Schema Creation - Added a Clear Button to the Type and Field Option Modals
* Schema Creation - Fixed Info section unlocked from top of schema
* Transformation - Fixed schema deletion issue
* Generation - Prevent unresolved schemas from generating messages

## v0.7.1

* Fixed pydantic reserved word validation logic
* Updated translation error handling

## v0.7.0

* Fixed arrayOf validation logic
* Fixed min/max length validation logic
* Create Schema: Allow the user to highlight or star the Type they are working on
* Dependencies updated
  * @‌babel/core ^7.21.4 → ^7.23.0
  * @‌babel/eslint-parser ^7.21.3 → ^7.22.15
  * @‌babel/plugin-proposal-decorators ^7.21.0 → ^7.23.0
  * @‌babel/plugin-proposal-do-expressions ^7.18.6 → ^7.22.5
  * @‌babel/plugin-proposal-export-default-from ^7.18.10 → ^7.22.17
  * @‌babel/plugin-proposal-function-bind ^7.18.9 → ^7.22.5
  * @‌babel/plugin-proposal-function-sent ^7.18.6 → ^7.22.5
  * @‌babel/plugin-proposal-pipeline-operator ^7.18.9 → ^7.22.15
  * @‌babel/plugin-proposal-throw-expressions ^7.18.6 → ^7.22.5
  * @‌babel/plugin-transform-react-constant-elements ^7.21.3 → ^7.22.5
  * @‌babel/plugin-transform-react-inline-elements ^7.21.0 → ^7.22.5
  * @‌babel/plugin-transform-runtime ^7.21.4 → ^7.22.15
  * @‌babel/preset-env ^7.21.4 → ^7.22.20
  * @‌babel/preset-react ^7.18.6 → ^7.22.15
  * @‌babel/preset-typescript ^7.21.4 → ^7.23.0
  * @‌babel/register ^7.21.0 → ^7.22.15
  * @‌babel/runtime ^7.21.0 → ^7.23.1
  * @‌fortawesome/fontawesome-svg-core ^6.4.0 → ^6.4.2
  * @‌fortawesome/free-solid-svg-icons ^6.4.0 → ^6.4.2
  * @‌types/d3-graphviz ^2.6.7 → ^2.6.8
  * @‌types/jest ^29.5.1 → ^29.5.5
  * @‌types/lodash ^4.14.194 → ^4.14.199
  * @‌types/node ^18.16.1 → ^20.8.4
  * @‌types/react ^18.2.0 → ^18.2.27
  * @‌types/react-dom ^18.2.1 → ^18.2.12
  * @‌types/react-redux ^7.1.25 → ^7.1.27
  * @‌types/redux-api-middleware ^3.2.3 → ^3.2.4
  * @‌types/redux-logger ^3.0.9 → ^3.0.10
  * @‌types/uuid ^9.0.1 → ^9.0.5
  * @‌types/webpack ^5.28.1 → ^5.28.3
  * @‌types/webpack-env ^1.18.0 → ^1.18.2
  * @‌typescript-eslint/eslint-plugin ^5.59.1 → ^6.7.5
  * @‌typescript-eslint/parser ^5.59.1 → ^6.7.5
  * @‌uiw/codemirror-extensions-langs ^4.19.16 → ^4.21.19
  * @‌uiw/codemirror-themes-all ^4.19.16 → ^4.21.19
  * @‌uiw/react-codemirror ^4.19.16 → ^4.21.19
  * babel-loader ^9.1.2 → ^9.1.3
  * css-loader ^6.7.3 → ^6.8.1
  * d3-graphviz ^5.0.2 → ^5.1.0
  * dayjs ^1.11.7 → ^1.11.10
  * eslint ^8.39.0 → ^8.51.0
  * eslint-config-prettier ^8.8.0 → ^9.0.0
  * eslint-import-resolver-typescript ^3.5.5 → ^3.6.1
  * eslint-import-resolver-webpack ^0.13.2 → ^0.13.7
  * eslint-plugin-compat ^4.1.4 → ^4.2.0
  * eslint-plugin-eslint-plugin ^5.0.8 → ^5.1.1
  * eslint-plugin-import ^2.27.5 → ^2.28.1
  * eslint-plugin-jest ^27.2.1 → ^27.4.2
  * eslint-plugin-prettier ^4.2.1 → ^5.0.0
  * eslint-plugin-react ^7.32.2 → ^7.33.2
  * html-react-parser ^3.0.16 → ^4.2.2
  * html-webpack-plugin ^5.5.1 → ^5.5.3
  * jest ^29.5.0 → ^29.7.0
  * marked ^4.3.0 → ^9.1.0
  * mini-css-extract-plugin ^2.7.5 → ^2.7.6
  * node-sass ^8.0.0 → ^9.0.0
  * prettier ^2.8.8 → ^3.0.3
  * react-redux ^8.0.5 → ^8.1.3
  * react-router-dom ^6.10.0 → ^6.16.0
  * react-select ^5.7.4 → ^5.7.7
  * react-toastify ^9.1.2 → ^9.1.3
  * react-zoom-pan-pinch ^3.0.7 → ^3.1.0
  * reactstrap ^9.1.9 → ^9.2.0
  * sass-loader ^13.2.2 → ^13.3.2
  * style-loader ^3.3.2 → ^3.3.3
  * terser-webpack-plugin ^5.3.7 → ^5.3.9
  * typescript ^4.9.5 → ^5.2.2
  * uuid ^9.0.0 → ^9.0.1
  * webpack ^5.81.0 → ^5.88.2
  * webpack-bundle-analyzer 4.8.0 → 4.9.1
  * webpack-cli ^5.0.2 → ^5.1.4
  * webpack-dev-server ^4.13.3 → ^4.15.1
  * webpack-merge ^5.8.0 → ^5.9.0
  * workbox-webpack-plugin ^6.5.4 → ^7.0.0

## v0.6.0

* Fixed field re-rendering issue
* Fixed multi schema uploading logic
* Improved field UI design
* Changed accordion logic to multicollapse
* Added insert at index Logic
* Added button style outline
* Added logic to check for duplicate Type names

## v0.5.2

* Visually nested child input fields under parent input fields
* Fixed unwanted auto scroll up on Field Option modal save
* Fixed Field Option modal popup on Drag and Drop
* Fixed unwanted auto scroll up on Type Option modal save
* Fixed Field Option - Collection Option selection error handling
* Updated Scroll To functionality, improved placement and visual representation
* Improved visual consistency
* Improved logic for the drag and drop duplicate Type and Field names
* Improved field drag and drop logic
* Improved field ID logic for Record and Array Type
* Included Show/Hide buttons for Types and Fields
* Included improved Add/Remove buttons for Fields
* Added Scroll To Top button
* Added ability to remove fields by index
* Added missing ArrayOf and MapOf fields
* Applied a fixed drag and drop scroll to

## v0.5.1

* Missing Field Options added
* Field Add auto scroll disabled
* Config label columns increased
* Input field size increased

## v0.5.0

* Introduced draggable types and fields
* Outline View for drag and drop reordering types
* Provided a non drag and drop option via button clicks
* General Schema Creation UI cleanup
* Expand or Collapse Info, Types and Fields
* Added scrollable inner sections for Schema Creation
* Improved color contrast

## v0.4.0

* Provided the ability to include namespaces and validate

## v0.3.0

* Introduced the ability to save Schemas and Messages. The saved file will persist for the lifetime of the local docker image.
* Implemented the Schema Transformation logic, which will convert one or more JADN Schemas into a different but related Schema (resolve references and strip comments).
* Implemented the Example Message Generation, which will generate various example messages based off of a Schema.
* Improved the drop down capability to include filtering and various usability improvements.

## v0.2.0 and v0.1.0

* Initial standup
