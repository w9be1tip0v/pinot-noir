## :hatched_chick: Project Pinot Noir
This is an application to summarize the PDF files using Gemini API.
Furthermore, this will be used to get important informations from financial documents stored.

### :rocket: Usage for Developers
The application is developed via devcontainer and docker, therefore you can develop it the same environment locally using .devcontainer/devcontainer.json.<BR>
Developers need setup API_KEY, which is generated at [Google AI Studio](https://ai.google.dev/).


```tree
your-LOCAL-repository/
├── .secrets
│   ├── config.toml
│   └── secrets.toml # Make sure to gitignore this!
├── your_app.py
└── requirements.txt
```

```toml, secrets.toml
GOOGLE_API_KEY = "Y0UR_GOOGLE_API_KEY_HERE"
```

For more informations, read the [official documents](https://ai.google.dev/gemini-api/docs).

### :bulb: Tips
The application is fully depended on Gemini API.<BR>
IF the app shows error status 4XX or 5XX, PLEASE CHECK YOUR API KEY AND GOOGLE API SERVER STATUS BELOW.
