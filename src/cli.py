import typer
from rich.console import Console
from rich.panel import Panel
from hackclub_ai import ask_hackclub, generate_better_prompt
from typing import List

console = Console()
app = typer.Typer(add_completion=False,help="🧠 AI Prompt Engineering Toolkit - Transform bad prompts into expert-level ones. To get help on certain commands type: ./prompt-toolkit-<os> COMMAND --help")

@app.command()
def improve(
    intent: str = typer.Argument(..., help="Intent for prompt optimization (e.g., summarize, rewrite, explain)"),
    text: List[str] = typer.Argument(..., help="Text to create optimized prompt for"),
    show_prompt: bool = typer.Option(True, "--show-prompt/--hide-prompt", help="Show the generated prompt"),
    ai: bool = typer.Option(False, "--ai", "-a", help="Get AI response using HackClub AI service")
):
    """Generate an optimized prompt using AI, then optionally get the response."""
    
    full_text = " ".join(text)
    
    # Use AI to generate a better prompt
    console.print("[blue]🧠 AI is crafting an optimized prompt...[/blue]")
    engineered_prompt = generate_better_prompt(intent, full_text)
    
    if show_prompt:
        console.print("\n")
        console.print(Panel(
            engineered_prompt,
            title="🔧 AI-Generated Optimized Prompt",
            border_style="yellow"
        ))
    
    if ai:
        console.print("\n[blue]🤖 Getting AI response with optimized prompt...[/blue]")
        response = ask_hackclub(engineered_prompt)
        console.print("\n")
        console.print(Panel(
            response,
            title="✨ AI Response",
            border_style="green"
        ))
    else:
        console.print("\n💡 [blue]Copy this optimized prompt and use it in ChatGPT, Claude, or any AI service or use hackclub ai services by simply adding the flag -a or --ai![/blue]")

@app.command()
def intents():
    """List available prompt improvement intents."""
    intents_list = [
        "summarize - Create concise summaries",
        "rewrite - Improve clarity and style", 
        "questions - Generate thoughtful questions",
        "explain - Break down complex concepts",
        "brainstorm - Generate creative ideas",
        "analyze - Deep analytical insights",
        "debug - Troubleshoot problems",
        "plan - Create step-by-step plans"
    ]
    
    console.print("\n[blue]📚 Available Intent Types:[/blue]\n")
    for intent in intents_list:
        console.print(f"[yellow]• {intent}[/yellow]")
    console.print("\n[dim]You can also use any custom intent like 'translate', 'critique', 'compare', etc.[/dim]")

if __name__ == "__main__":
    app()
