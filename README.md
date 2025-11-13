# SIPOC Diagram Template - Data Editing Guide

This guide explains how to edit the JSON data embedded in the SIPOC diagram template to customize it for your process.

## Overview

The SIPOC diagram uses a JSON data structure embedded in the HTML file within a `<script>` tag with `id="embedded-data"`. You can edit this data directly in the HTML file to customize your diagram.

## JSON Structure

The data is organized into five main sections:

\`\`\`json
{
  "suppliers": [...],
  "inputs": [...],
  "process": [...],
  "outputs": [...],
  "customers": [...],
  "connections": [...]
}
\`\`\`

## Editing Nodes

### Suppliers
Each supplier node has the following structure:

\`\`\`json
{
  "id": "supplier-1",
  "name": "Raw Material Vendors",
  "description": "Suppliers providing raw materials and components",
  "requirements": "ISO 9001 certification, on-time delivery, quality consistency"
}
\`\`\`

- **id**: Unique identifier (must be unique across all nodes)
- **name**: Display name shown on the diagram
- **description**: Detailed information shown in the side panel
- **requirements**: Specific requirements or criteria for this supplier

### Inputs
\`\`\`json
{
  "id": "input-1",
  "name": "Raw Materials",
  "description": "Primary materials required for manufacturing",
  "specifications": "Grade A steel, polymer compounds, electronic components"
}
\`\`\`

- **specifications**: Technical specifications for the input

### Process Steps
\`\`\`json
{
  "id": "process-start",
  "name": "START",
  "description": "Process initiation point",
  "activities": "Receive order, verify requirements, allocate resources"
}
\`\`\`

- **activities**: Actions performed at this process step

### Outputs
\`\`\`json
{
  "id": "output-1",
  "name": "Finished Products",
  "description": "Completed manufactured goods",
  "deliverables": "Tested and packaged products ready for shipment"
}
\`\`\`

- **deliverables**: What is produced at this stage

### Customers
\`\`\`json
{
  "id": "customer-1",
  "name": "Industrial Manufacturers",
  "description": "B2B customers in manufacturing sector",
  "segment": "Large-scale industrial operations requiring bulk orders"
}
\`\`\`

- **segment**: Customer segment or category

## Creating Connections

Connections define the relationships between nodes. Each connection has:

\`\`\`json
{
  "from": "supplier-1",
  "to": "input-1"
}
\`\`\`

- **from**: ID of the source node
- **to**: ID of the destination node

### Connection Rules

1. **Suppliers → Inputs**: Show which supplier provides which inputs
2. **Inputs → Process**: Show which inputs are used in which process steps
3. **Process → Outputs**: Show which process steps produce which outputs
4. **Outputs → Customers**: Show which outputs go to which customers

### Example Connection Flow
\`\`\`json
{
  "connections": [
    { "from": "supplier-1", "to": "input-1" },
    { "from": "supplier-1", "to": "input-2" },
    { "from": "input-1", "to": "process-1" },
    { "from": "process-1", "to": "output-1" },
    { "from": "output-1", "to": "customer-1" }
  ]
}
\`\`\`

## Adding New Nodes

To add a new node:

1. **Choose the section** (suppliers, inputs, process, outputs, or customers)
2. **Copy an existing node** structure from that section
3. **Update the ID** to be unique (e.g., "input-9" if you have 8 inputs)
4. **Edit the name and details** for your new node
5. **Add connections** to show relationships with other nodes

### Example: Adding a New Input

\`\`\`json
{
  "id": "input-9",
  "name": "Quality Control Tools",
  "description": "Testing and inspection equipment",
  "specifications": "Calibrated measuring devices, inspection software"
}
\`\`\`

Then add connections:
\`\`\`json
{ "from": "supplier-3", "to": "input-9" },
{ "from": "input-9", "to": "process-3" }
\`\`\`

## Removing Nodes

To remove a node:

1. **Delete the node** from its section array
2. **Remove all connections** that reference that node's ID (both `from` and `to`)

## Best Practices

1. **Keep IDs consistent**: Use the format `category-number` (e.g., "supplier-1", "input-5")
2. **Unique IDs**: Never reuse IDs across different nodes
3. **Meaningful names**: Use clear, concise names (they appear on the diagram)
4. **Detailed descriptions**: Add comprehensive details (shown in the side panel)
5. **Logical connections**: Only connect nodes between adjacent SIPOC levels
6. **Avoid crossing connections**: Try to arrange nodes to minimize line crossings

## Testing Your Changes

After editing the data:

1. **Save the HTML file**
2. **Refresh your browser**
3. **Click on nodes** to verify descriptions appear correctly
4. **Check connections** are drawn between the correct nodes
5. **Verify highlighted connections** when clicking nodes

## Common Issues

### Connections Not Appearing
- Check that both `from` and `to` IDs exist in your node data
- Ensure IDs match exactly (case-sensitive)

### Side Panel Shows "No details available"
- Verify the node has a `description` field
- Check for JSON syntax errors (missing commas, quotes)

### Nodes Overlapping
- Reduce the number of nodes per row
- Adjust node spacing in the CSS if needed

## Example: Complete Custom SIPOC

Here's a minimal example for a simple process:

\`\`\`json
{
  "suppliers": [
    {
      "id": "supplier-1",
      "name": "Vendor A",
      "description": "Primary supplier",
      "requirements": "Quality standards"
    }
  ],
  "inputs": [
    {
      "id": "input-1",
      "name": "Materials",
      "description": "Raw materials",
      "specifications": "Grade A"
    }
  ],
  "process": [
    {
      "id": "process-start",
      "name": "START",
      "description": "Begin process",
      "activities": "Initialize"
    },
    {
      "id": "process-1",
      "name": "Step 1",
      "description": "First step",
      "activities": "Process materials"
    }
  ],
  "outputs": [
    {
      "id": "output-1",
      "name": "Product",
      "description": "Finished product",
      "deliverables": "Packaged item"
    }
  ],
  "customers": [
    {
      "id": "customer-1",
      "name": "End User",
      "description": "Final customer",
      "segment": "Retail"
    }
  ],
  "connections": [
    { "from": "supplier-1", "to": "input-1" },
    { "from": "input-1", "to": "process-1" },
    { "from": "process-1", "to": "output-1" },
    { "from": "output-1", "to": "customer-1" }
  ]
}
\`\`\`

## Customizing Colors

The SIPOC diagram uses a professional color scheme that can be customized by editing the CSS in the HTML file.

### Color Scheme Structure

The diagram has five distinct color categories:

1. **Suppliers** - Dark teal/blue (#3d6978)
2. **Inputs** - Teal (#4a7c7e)
3. **Process** - Olive green (#6b7c3f)
4. **Outputs** - Warm brown/orange (#b8763e)
5. **Customers** - Burgundy/wine (#7d4a5c)

### Where to Find Colors in the HTML

Open the HTML file and locate the `<style>` section. Look for these CSS classes:

\`\`\`css
.node.suppliers { background: #3d6978; }
.node.inputs { background: #4a7c7e; }
.node.process { background: #6b7c3f; }
.node.outputs { background: #b8763e; }
.node.customers { background: #7d4a5c; }
\`\`\`

### Changing Category Colors

To change a category's color, replace the hex color code:

\`\`\`css
/* Original */
.node.suppliers { background: #3d6978; }

/* Custom - bright blue */
.node.suppliers { background: #2563eb; }
\`\`\`

### Changing Label Colors

The left-side labels have corresponding colors:

\`\`\`css
.label.suppliers { background: #3d6978; }
.label.inputs { background: #4a7c7e; }
.label.process { background: #6b7c3f; }
.label.outputs { background: #b8763e; }
.label.customers { background: #7d4a5c; }
\`\`\`

Make sure to update both the node and label colors to match.

### Hover Effect Colors

Each category has a hover state that lightens on interaction:

\`\`\`css
.node.suppliers:hover { background: #4a7f91; }
.node.inputs:hover { background: #5a9294; }
.node.process:hover { background: #7d9451; }
.node.outputs:hover { background: #c98a52; }
.node.customers:hover { background: #925c6f; }
\`\`\`

To create a hover color, use a lighter shade of your base color (typically 10-15% lighter).

### Connection Line Colors

Connection lines are light gray by default:

\`\`\`css
.connection-line {
  stroke: #d1d5db;
  stroke-width: 2;
  fill: none;
}

.connection-line.active {
  stroke: #f59e0b;
  stroke-width: 3;
}
\`\`\`

- **Default state**: `stroke: #d1d5db;` (light gray)
- **Active/highlighted state**: `stroke: #f59e0b;` (amber/gold)

### Side Panel Colors

The side panel header colors match the node categories:

\`\`\`css
.panel-header.suppliers { background: #3d6978; }
.panel-header.inputs { background: #4a7c7e; }
.panel-header.process { background: #6b7c3f; }
.panel-header.outputs { background: #b8763e; }
.panel-header.customers { background: #7d4a5c; }
\`\`\`

### Complete Color Change Example

To change the entire Suppliers category to a corporate blue:

\`\`\`css
/* Nodes */
.node.suppliers { background: #1e40af; }
.node.suppliers:hover { background: #2563eb; }

/* Labels */
.label.suppliers { background: #1e40af; }

/* Side panel header */
.panel-header.suppliers { background: #1e40af; }
\`\`\`

### Color Selection Tips

1. **Maintain contrast**: Ensure text remains readable (white text works best on dark backgrounds)
2. **Use distinct colors**: Each category should be clearly distinguishable
3. **Consistent saturation**: Keep similar saturation levels across categories for visual harmony
4. **Test accessibility**: Verify colors meet WCAG contrast requirements
5. **Professional palette**: Muted, sophisticated colors work better than bright, saturated ones

### Recommended Color Palettes

**Corporate Blue Theme:**
- Suppliers: #1e3a8a (navy)
- Inputs: #0ea5e9 (sky blue)
- Process: #06b6d4 (cyan)
- Outputs: #8b5cf6 (purple)
- Customers: #6366f1 (indigo)

**Earth Tones Theme:**
- Suppliers: #78350f (dark brown)
- Inputs: #92400e (burnt orange)
- Process: #365314 (dark green)
- Outputs: #a16207 (amber)
- Customers: #831843 (burgundy)

**Modern Tech Theme:**
- Suppliers: #1f2937 (gray-800)
- Inputs: #374151 (gray-700)
- Process: #4b5563 (gray-600)
- Outputs: #6b7280 (gray-500)
- Customers: #9ca3af (gray-400)

### Testing Your Color Changes

After changing colors:
1. Save the HTML file
2. Refresh your browser
3. Check all five categories appear correctly
4. Verify hover states work
5. Click nodes to confirm side panel headers match
6. Ensure connection lines remain visible

### Using CSS Color Formats

You can use different color formats:

\`\`\`css
/* Hex */
.node.suppliers { background: #3d6978; }

/* RGB */
.node.suppliers { background: rgb(61, 105, 120); }

/* RGBA (with transparency) */
.node.suppliers { background: rgba(61, 105, 120, 0.9); }

/* HSL */
.node.suppliers { background: hsl(196, 32%, 35%); }
\`\`\`

Hex codes are recommended for simplicity and consistency.
DONE