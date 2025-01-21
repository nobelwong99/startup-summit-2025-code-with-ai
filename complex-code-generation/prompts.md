## Frontend Code Generation

You are a frontend developer specialising in nextjs, tailwindcss and shadcn ui. Use npx shadcn@latest to add shadcn components to the project.

Build a modern and responsive SaaS landing page with all the essential components and pages. Include the following

1. hero
2. features
3. pricing
4. testimonial
5. call to action
6. contact us

I want to add a dashboard button to the nav bar on the right, when clicked, direct user to /dashboard, keep the page empty for now.

Create a nav bar at the top for quick navigation. Use shadcn components to build the pages, add animation and slight gradients while keeping a minimalist look and feel.

@Shadcn In the dashboad page, I want to create a simple business dasboard with tables, charts and widgets. Use animation icons and charts to display these components

1. Create a sidebar navigation using shadcn
2. create multiple mock tabs in the navigation
3. Create the dashboard with the components specified above

Create the customer page to display our existing customers and a add customer button which will open up a form dialog to create new customer. use mock data to populate the customer table

## Python Demo Code Generation

### Prompt

Create a Python command-line interface (CLI) app for managing tasks. The app should:

1. Allow users to:

   - Add a new task with a name and optional due date.
   - List all tasks, categorized as pending or completed.
   - Mark a task as completed by its task ID.
   - Export the task list to a JSON file.

2. Use a dictionary to store tasks, with each task having:

   - A unique ID (integer, auto-incremented).
   - Name (string).
   - Due date (string, optional).
   - Completion status (boolean).

3. Save the tasks to a local json file for data persistency instead of storing in memory which will get cleared everytime the python code exits.

4. Include error handling for invalid inputs and edge cases (e.g., trying to complete a non-existent task).

5. Keep the code well-organized and include comments for clarity.

Write the complete code.

## Iteration 1

### Prompt

Update the code to add a delete command to the CLI app. The app should:

1. Allow users to delete a task by its task ID.

2. Include error handling for invalid inputs and edge cases (e.g., trying to delete a non-existent task).

3. Keep the code well-organized and include comments for clarity.

Write the complete code.

## Iteration 2

### Prompt

Update the code so when no due date is provided, the task is set to be due in 1 day.

## Iteration 3

### Prompt

Create a readme file to document what the cli app does, how to use it and the prompt that can be used to generate this exact app using a LLM

command + shift + v to preview markdown
