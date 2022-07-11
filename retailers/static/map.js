// Declaration of basemap layers.
const mapnik_url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const mapnik_attribute = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors | <a href='https://www.flaticon.com/' title='Flaticon icons'>Icons created by Smashicons - Flaticon</a>";
const mapnik = L.tileLayer(mapnik_url, { attribution: mapnik_attribute });
{/* <a href="https://www.flaticon.com/free-icons/gas" title="gas icons">Gas icons created by Smashicons - Flaticon</a> */}

const CartoDB_Dark = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
  attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
});


const baseLayers = {
  'Day': mapnik,
  'Night': CartoDB_Dark
};


//Set variable constant to filter petroleum products to filter out products not in stock.
const filter_list = [true];


//Function to load markers from the site's API as GeoJSON objects.
async function load_markers() {
  const markers_url = `/api/retailers/?in_bbox=${map.getBounds().toBBoxString()}`
  const response = await fetch(markers_url)
  const geojson = await response.json()
  return geojson
}


//Function to filter in only stations that have PMS (petrol) in stock.
function pmsInStockFilter(layer) {
  return filter_list.includes(layer.properties.pms_stock)
}

//Function to filter in only stations that have AGO (diesel) in stock.
function agoInStockFilter(layer) {
  return filter_list.includes(layer.properties.ago_stock)
}

//Function to filter in only stations that have DPK (kerosene) in stock.
function dpkInStockFilter(layer) {
  return filter_list.includes(layer.properties.dpk_stock)
}

//Function to filter in only stations that have LPG (cooking gas) in stock.
function lpgInStockFilter(layer) {
  return filter_list.includes(layer.properties.lpg_stock)
}

//Function to filter in only stations that have an Auto Shop.
function autoShopFilter(layer) {
  return filter_list.includes(layer.properties.auto_shop)
} 

//Function to filter in only stations that have a Supermart.
function superMartFilter(layer) {
  return filter_list.includes(layer.properties.supermart)
}

//Function to filter in only stations that have a Car Wash.
function carWashFilter(layer) {
  return filter_list.includes(layer.properties.car_wash)
}


//Declaration of icon and settings for PMS markers.
var pms_Icon = new L.icon({
  iconUrl: "/static/images/petrol-pump 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var pms_pump = new L.LayerGroup();
async function render_pms_markers() {
  const pms_markers = await load_markers();
  L.geoJSON(pms_markers, {
    filter: pmsInStockFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: pms_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'Petrol price per litre: ₦' + layer.feature.properties.pms_rate
    + '<br/>' + 'In stock: ' + layer.feature.properties.pms_stock
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
    )
    
    .addTo(pms_pump);
}


//Declaration of icon and settings for AGO (diesel) markers.
var ago_Icon = new L.icon({
  iconUrl: "/static/images/diesel-pump 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var ago_pump = new L.LayerGroup();
async function render_ago_markers() {
  const ago_markers = await load_markers();
  L.geoJSON(ago_markers, {
    filter: agoInStockFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: ago_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'Diesel price per litre: ₦' + layer.feature.properties.ago_rate
    + '<br/>' + 'In stock: ' + layer.feature.properties.ago_stock
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(ago_pump);
}


//Declaration of icon and settings for DPK (Kerosene) markers.
var dpk_Icon = new L.icon({
  iconUrl: "/static/images/kerosene-pump 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var dpk_pump = new L.LayerGroup();
async function render_dpk_markers() {
  const dpk_markers = await load_markers();
  L.geoJSON(dpk_markers, {
    filter: dpkInStockFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: dpk_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name     
    + '<br/>' + 'Kerosene price per litre: ₦' + layer.feature.properties.dpk_rate
    + '<br/>' + 'In stock: ' + layer.feature.properties.dpk_stock
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(dpk_pump);
}


//Declaration of icon and settings for LPG (Cooking Gas) markers.
var lpg_Icon = new L.icon({
  iconUrl: "/static/images/gas 64px.png",
  iconSize:     [50, 50], // size of the icon
  iconAnchor:   [24, 48], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var lpg_pump = new L.LayerGroup();
async function render_lpg_markers() {
  const lpg_markers = await load_markers();
  L.geoJSON(lpg_markers, {
    filter: lpgInStockFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: lpg_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'LPG price per kg: ₦' + layer.feature.properties.lpg_rate
    + '<br/>' + 'In stock: ' + layer.feature.properties.lpg_stock
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(lpg_pump);
}


// A layer that removes all energy products from the map display.
var clear_all = new L.LayerGroup();


//Declaration of icon and settings for PMS markers.
var autoshop_Icon = new L.icon({
  iconUrl: "/static/images/garage 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var autoshop = new L.LayerGroup();
async function render_autoshop_markers() {
  const autoshop_markers = await load_markers();
  L.geoJSON(autoshop_markers, {
    filter: autoShopFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: autoshop_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'Service: ' + 'Autoshop'
    + '<br/>' + 'Open: ' + layer.feature.properties.auto_shop
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(autoshop);
}


//Declaration of icon and settings for Supermart markers.
var supermart_Icon = new L.icon({
  iconUrl: "/static/images/shopping-cart 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var supermart = new L.LayerGroup();
async function render_supermart_markers() {
  const supermart_markers = await load_markers();
  L.geoJSON(supermart_markers, {
    filter: superMartFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: supermart_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'Service: ' + 'Supermart'
    + '<br/>' + 'Open: ' + layer.feature.properties.supermart
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(supermart);
}


//Declaration of icon and settings for Car Wash markers.
var carwash_Icon = new L.icon({
  iconUrl: "/static/images/car-wash 64px.png",
  iconSize:     [42, 42], // size of the icon
  iconAnchor:   [21, 42], // point of the icon which will correspond to marker's location
  popupAnchor:  [0, -32] // point from which the popup should open relative to the iconAnchor
});

var carwash = new L.LayerGroup();
async function render_carwash_markers() {
  const carwash_markers = await load_markers();
  L.geoJSON(carwash_markers, {
    filter: carWashFilter,
    pointToLayer: function(feature,latlng){
      return L.marker(latlng,{icon: carwash_Icon});
    }
  })
    .bindPopup(
      (layer) => 'Name: ' + layer.feature.properties.name      
    + '<br/>' + 'Service: ' + 'Car Wash'
    + '<br/>' + 'Open: ' + layer.feature.properties.car_wash
    + '<br/>' + 'Phone: ' + layer.feature.properties.phone
      )
    .addTo(carwash);
}



// Set 'mapnik' and 'pms_pump' (petrol pumps) constants to be the default 
// basemap and energy product to be displayed respectively.
const map = L.map("map", { layers: [mapnik, pms_pump], minZoom: 4 });

/* map.locate()
  .on("locationfound", (e) => map.setView(e.latlng, 14))
  .on("locationerror", () => map.setView([0, 0], 6)); */

map.setView([8.895, 7.24], 13);


// Overlay layers are grouped
var groupedOverlays = {
  "<span style='font-weight: bold;'>Energy Products (In Stock)</span>": {
    "Petrol": pms_pump,
    "Diesel": ago_pump,
    "Kerosene": dpk_pump,
    "Cooking Gas": lpg_pump,
    "Clear All": clear_all
  },
  "<span style='font-weight: bold;'>Extras</span>": {
    "Auto Shop": autoshop,
    "Supermart": supermart,
    "Car Wash": carwash,
  }
};


//Render PMS markers when the mouse is moved or the map panned.
map.on("pageshow", render_pms_markers);
map.on("mouseover", render_pms_markers);
map.on("moveend", render_pms_markers);

//Render AGO markers when the mouse is moved or the map panned.
map.on("mouseover", render_ago_markers);
map.on("moveend", render_ago_markers);

//Render DPK markers when the mouse is moved or the map panned.
map.on("mouseover", render_dpk_markers);
map.on("moveend", render_dpk_markers);

//Render LPG markers when the mouse is moved or the map panned.
map.on("mouseover", render_lpg_markers);
map.on("moveend", render_lpg_markers);

//Render Autoshop markers when the mouse is moved or the map panned.
map.on("mouseover", render_autoshop_markers);
map.on("moveend", render_autoshop_markers);

//Render Supermart markers when the mouse is moved or the map panned.
map.on("mouseover", render_supermart_markers);
map.on("moveend", render_supermart_markers);

//Render Car Wash markers when the mouse is moved or the map panned.
map.on("mouseover", render_carwash_markers);
map.on("moveend", render_carwash_markers);



var options = {
  // Radio buttons to ensure a user views the distrbution of only one energy product at a time
  exclusiveGroups: ["<span style='font-weight: bold;'>Energy Products (In Stock)</span>"],
  // Disable "one click select all" checkbox for 'Extras' (and any non-exclusive group).
  groupCheckboxes: false
};

// var layerControl = L.control.layers(baseLayers).addTo(map);

// Use the custom grouped layer control, not "L.control.layers"
var layerControl = L.control.groupedLayers(baseLayers, groupedOverlays, options).addTo(map);