<h1>In this project I learn how to create templates (.html) in the project</h1>
<h2>Process to create templates in the Django Project</h2>
<h3>1. Create one project:</h3>
<p>Use the command <code>django-admin startproject project_name</code> to create a new Django project.</p>
<h3>2. Create an application:</h3>
<p>Navigate into the project directory and use the command <code>python manage.py startapp app_name</code> to create a new app.</p>
<h3>3. Register the app in settings.py:</h3>
<p>In the project's <code>settings.py</code>, add the app name to the <code>INSTALLED_APPS</code> list.</p>
<h3>4. Create a folder named templates inside the outer project:</h3>
<p>Inside the main project directory (same level as <code>settings.py</code>), create a folder named <code>templates</code>. Inside this folder, you can create subdirectories for each app if needed.</p>
<h3>5. Configure the template directory in settings.py:</h3>
<p>In <code>settings.py</code>, add the path to the <code>templates</code> folder in the <code>TEMPLATES</code> setting, under the <code>'DIRS'</code> key.</p>
<h3>6. Create a template file:</h3>
<p>Inside the <code>templates</code> folder, create an HTML file (e.g., <code>index.html</code>).</p>
<h3>7. Create a function-based view in views.py:</h3>
<p>In your app's <code>views.py</code>, create a view function that will render the template using Django’s <code>render</code> function.</p>
<h3>8. Set the path in urls.py:</h3>
<p>In your app’s <code>urls.py</code>, define a URL pattern that points to the view function. Then include your app’s <code>urls.py</code> in the main project’s <code>urls.py</code> file.</p>
<h3>9. Run the project:</h3>
<p>Use the command <code>python manage.py runserver</code> to start the development server.</p>
<h3>10. Test and refine:</h3>
<p>Navigate to the URL you defined in the browser to see your template rendered. Make any
