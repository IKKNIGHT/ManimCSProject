# ManimCSProject

A simple Manim Project.

## Key Features & Benefits

This project utilizes the Manim library to create educational animations, specifically focusing on explaining Internet addressing concepts like IPv4, IPv6, and MAC addresses.

*   Clear and visually engaging explanations.
*   Demonstrates the use of Manim for creating educational content.

## Prerequisites & Dependencies

Before running this project, ensure you have the following installed:

*   **Python:** Version 3.6 or higher.
*   **Manim:** Installation instructions can be found on the official [Manim documentation](https://www.manim.community/).  Use `pip install manim`.
*   **LaTeX:**  Manim requires LaTeX for rendering mathematical equations. Install a TeX distribution like TeX Live or MiKTeX.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/IKKNIGHT/ManimCSProject.git
    cd ManimCSProject
    ```

2.  **Install Manim (if not already installed):**

    ```bash
    pip install manim
    ```

3.  **Install required Python packages (if any are listed in a requirements.txt):**

    ```bash
    #If a requirements.txt file exists
    pip install -r requirements.txt
    ```

## Usage Examples & API Documentation

To render the animation, run the following command:

```bash
manim -pql main.py IPAddressExplainer
```

This command will render the `IPAddressExplainer` scene from the `main.py` file at low quality ( `-ql`) suitable for quick previews. For higher quality renderings, use `-pqm` or `-pqh`.

**API Usage (Manim)**

The core of this project relies on the Manim library. Refer to the official Manim documentation for detailed API usage and customization options: [https://docs.manim.community/en/stable/](https://docs.manim.community/en/stable/)

Example from `main.py`:

```python
from manim import *

class IPAddressExplainer(Scene):
    def construct(self):
        # === TITLE ===
        title = Text("Internet Addressing: IPv4, IPv6, and MAC Addresses", font_size=40, color=YELLOW)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.to_edge(UP))

        # === INTRODUCTION ===
        intro = Text(
            "Every networked device must have a unique identifier to send and receive data.",
            font_size=25
        )
        self.play(Write(intro))
        self.wait(2)
        self.play(Unwrite(intro))
```

This snippet shows how to create a title text and introduction text using Manim's `Text` class and animate them onto the screen using `Write` and `Unwrite` animations.

## Configuration Options

Currently, there are no explicit configuration options defined within the project beyond those available through Manim itself. You can modify parameters such as font size, colors, and animation speeds directly within the `main.py` file.  Refer to the Manim documentation for detailed configuration instructions.

## Contributing Guidelines

Contributions are welcome! To contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix:

    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  Make your changes and commit them:

    ```bash
    git add .
    git commit -m "Add your descriptive commit message"
    ```

4.  Push your changes to your forked repository:

    ```bash
    git push origin feature/your-feature-name
    ```

5.  Create a pull request to the main repository.

## License Information

License not specified. All rights reserved.

## Acknowledgments

This project utilizes the Manim library, created by Grant Sanderson and the Manim Community.  Thanks to the developers of Manim for creating such a powerful tool.
