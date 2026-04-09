// Fixed pattern: Set Content Security Policy (CSP) header to apply security best practices
const csp = 'default-src https:; object-src 'none'';
response.headers.set('Content-Security-Policy', csp);