## Implementation Guidance

### Beginner Friendly Approaches
1. Start with a Three.js scene and add orbit controls and a grid helper.
2. Load GLB assets with Draco/meshopt decoding; validate units and orientation.
3. Implement a material editor that exposes baseColor, roughness, metalness, and normal map toggles.
4. Add image-based lighting using an HDRI and enable ACES tone mapping.

### Intermediate Techniques
1. Add floor plan import (SVG/DXF). Snap walls to 90° and 45° angles. Auto-generate rooms and areas.
2. Implement asset instancing and per-room grouping; persist layouts to a JSON scene graph.
3. Integrate pricing via area takeoff for flooring/paint and BOM for furniture with SKU links.
4. Add AR export as USDZ/GLB, and publish a shareable viewer link.

### Expert Level Guidance
1. Enable path tracing or ReSTIR GI when WebGPU is available; fall back to PBR on WebGL2.
2. Compress textures to KTX2, generate mips, and use triplanar mapping for large surfaces.
3. Build IFC ingestion to map BIM properties to asset variants and finish schedules.
4. Implement server-side render queue with headless WebGPU where supported; attach denoisers.
