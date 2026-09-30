# Food and fluid behavior vocabulary

Specify the intended read through observable motion, scale and light response.
These are direction cues, not numerical fluid presets. Use measured project values
when implementing a simulation and verify the installed renderer/solver version.

## Material families

| Material | Motion cues | Surface/optical cues | Common false read |
|---|---|---|---|
| Water / clear broth | Fast gravity response, narrow stream, early breakup at low flow, quick leveling, impact-sized ripples | Transmission/refraction where appropriate, crisp moving highlights, visible depth/absorption | Glass slab, mercury, gel, detached glitter |
| Milk | More body and opacity than water but clearly freer-flowing than cream; stream narrows under gravity and ends in small residual drops; ripples level promptly | Soft white volume/subsurface read, restrained specular highlight, no chalk-solid edge | Cream, yogurt, icing or white paint forming a rope |
| Thin sauce / stock | Name the comparison substance and pour rate; coherent stream may persist longer than water but must still accelerate, impact and spread | Color absorption, wet highlight and receiver staining appropriate to the recipe | Generic syrup because “rich” or “velvety” overrode the intended flow |
| Thick sauce / glaze | Slower sheet or ribbon, stronger wall adhesion, delayed leveling and fewer satellite drops | Broader glossy highlight, visible coating thickness and wet edge | Rubber, slime, clay or a rigid extruded tube |
| Porridge / juk | Bulk moves slowly while the wet top surface deforms locally; stirring leaves a wake that relaxes; ingredient clusters remain suspended/embedded | Moist broken highlights over a mostly diffuse body; no plastic-perfect mirror | Milk soup with floating beads, mashed clay, aerated cream |
| Rice / grains | Individual pieces stay subordinate to bowl and spoon scale; local clusters follow the carrier or porridge instead of moving on one clock | Small wet highlights and partial occlusion; variation without species drift | Boba, beans, pebbles, corn kernels or oversized pellets |
| Oil / fat | Thin film can spread and form sharper moving highlights; droplets may bead depending on the receiving surface | Strong grazing-angle specular, possible separation from water phase | Metallic chrome, soap bubble rainbow unless requested |
| Steam / vapor | Starts above a credible hot source, rises with drift/turbulence, thins and dissipates; density responds to the event | Best revealed by local back/side light; semi-transparent and depth-aware | Opaque smoke column, floor fog, vapor appearing before heat |

## Pour lifecycle

Inspect all phases, not only the prettiest middle frame:

1. **Precondition:** substance is contained; no leak before tilt/opening.
2. **Onset:** the liquid reaches the downhill lip after the vessel changes orientation.
3. **Established flow:** stream leaves the actual mouth, accelerates, narrows or
   sheets according to the material, and stays connected when flow is continuous.
4. **Breakup:** lower flow or longer travel produces plausible necking and droplets;
   breakup is not random particles detached from the source.
5. **Impact:** receiver is under the exit; disturbance begins at the impact point.
6. **Response:** splash/ripple/wake amplitude matches fall height, flow and scene scale.
7. **Shutoff:** returning upright or closing the source reduces the stream, followed
   by only plausible residual drops.
8. **Final state:** volume resides in the named sink; wetness and residue remain
   where contact occurred and do not jump between surfaces.

## Scale discipline

- Define ingredient size relative to the vessel mouth, spoon bowl, hand or plate.
  Use absolute dimensions only when the scene is calibrated.
- Read scale at delivery resolution. A physically small grain that merges into a
  noisy blob may need lighting/contrast or a diagnostic close view, not enlargement
  in the projection master.
- Splash height, ripple wavelength, bubble size and steam eddy size all signal
  scene scale. Oversized secondary motion can make miniatures read as toys in gel.
- Preserve species and process: rice cannot grow into dumplings during a pour, and
  a smooth porridge may show fine grains without becoming a bowl of discrete pellets.

## Material response

- **Specular** communicates the reflective wet interface. State highlight width,
  motion and restraint; “glossy” alone often produces plastic.
- **Roughness** changes highlight spread, not viscosity. Do not use a roughness word
  as a substitute for motion behavior.
- **Subsurface/volume scattering** can soften milk or cooked grains, but excessive
  scattering creates wax, chalk or a glowing substance.
  In a calibrated miniature scene, inspect the shader's scattering distance/scale,
  not only its weight. Broad default distances can erase all small food relief;
  use the actual scene units and verify the result at delivery framing rather than
  copying one numerical preset to every dish.
- **Transmission/refraction** helps clear liquids; opacity and absorption still
  depend on substance and depth.
- **Wetness** is a localized coating/residue with a contact history. It should
  darken or sharpen highlights where the liquid actually touched, not coat the set.
- **Contact shadows and occlusion** ground vessels and grains but cannot repair an
  impossible stream path or a receiver that was never under the source.
