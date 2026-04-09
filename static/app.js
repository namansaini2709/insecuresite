# Set the Content-Security-Policy header to prevent XSS attacks
app.set('trust proxy', 1);
app.use((req, res, next) => {
  res.setHeader('Content-Security-Policy', 'default-src https: data: blob: ; script-src https://cdn.example.com ; object-src https://cdn.example.com');
  next();
});