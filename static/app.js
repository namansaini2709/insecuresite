app.use((req, res) => {
   res.setHeader('Content-Security-Policy', 'default-src https:; script-src https:;');
   res.setHeader('Strict-Transport-Security', 'max-age=63072000;');
   res.setHeader('X-Content-Type-Options', 'nosniff');
   res.setHeader('X-Frame-Options', 'DENY');
   res.setHeader('X-XSS-Protection', '1; mode=block');
});