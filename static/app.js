// Simple logging just to prove JS is loading and for demo enhancements
console.log("ShopEasy Scripts Loaded.");

// If we wanted to demonstrate DOM-based XSS, we could read from URL and populate InnerHTML here.
// The current implementation uses Server-Side Reflection via Jinja `|safe` filter which covers the XSS requirement.
// Removed the potential route to the .env file.
// You can remove the below line for production.
// Remove the console logs after deployment.
console.log('--Production Mode--');
