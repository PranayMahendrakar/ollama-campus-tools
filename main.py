#!/usr/bin/env python3
"""
Ollama Campus Life & Productivity Tools - 15 AI-Powered Student Assistants
Run: python main.py
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt

console = Console()

TOOLS = {
    1: ("Student Organization Matcher", "tools.org_matcher", "Find clubs that match your interests"),
    2: ("Campus Event Recommender", "tools.event_recommender", "Discover campus events"),
    3: ("Course Schedule Optimizer", "tools.schedule_optimizer", "Build the perfect schedule"),
    4: ("Group Project Role Allocator", "tools.group_allocator", "Optimize team roles"),
    5: ("Work-Study Balance Advisor", "tools.work_balance", "Balance work and academics"),
    6: ("Stress Management Coach", "tools.stress_coach", "Manage academic stress"),
    7: ("Campus Resource Locator", "tools.resource_locator", "Find campus resources"),
    8: ("Extracurricular Activity Planner", "tools.activity_planner", "Plan meaningful activities"),
    9: ("Meal Plan Optimization Tool", "tools.meal_optimizer", "Maximize your meal plan"),
    10: ("Dormitory Compatibility Matcher", "tools.roommate_matcher", "Find compatible roommates"),
    11: ("Digital Wellness Guide", "tools.digital_wellness", "Healthy tech habits"),
    12: ("Student Budget Advisor", "tools.budget_advisor", "Manage student finances"),
    13: ("Time Management Consultant", "tools.time_management", "Master your time"),
    14: ("College Life Transition Coach", "tools.transition_coach", "Navigate transitions"),
    15: ("Campus Sustainability Advisor", "tools.sustainability_advisor", "Live sustainably"),
}

def show_menu():
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🎓 Ollama Campus Life & Productivity Tools[/bold cyan]\n"
        "[dim]15 AI-Powered Tools for Students[/dim]",
        border_style="cyan"
    ))
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Tool", style="green", width=35)
    table.add_column("Description", style="dim")
    
    for num, (name, _, desc) in TOOLS.items():
        table.add_row(str(num), name, desc)
    
    table.add_row("0", "Exit", "Quit the application")
    console.print(table)
    console.print()

def run_tool(choice: int):
    if choice == 0:
        console.print("[yellow]Goodbye! Good luck with your studies! 🎓[/yellow]")
        sys.exit(0)
    
    if choice not in TOOLS:
        console.print("[red]Invalid choice. Please try again.[/red]")
        return
    
    name, module_path, _ = TOOLS[choice]
    console.print(f"\n[bold green]Starting {name}...[/bold green]\n")
    
    try:
        module = __import__(module_path, fromlist=['run'])
        module.run()
    except ImportError as e:
        console.print(f"[red]Error loading module: {e}[/red]")
    except Exception as e:
        console.print(f"[red]Error running tool: {e}[/red]")
    
    console.print("\n[dim]Press Enter to return to menu...[/dim]")
    input()

def main():
    try:
        import ollama
        ollama.list()
        console.print("[green]✓ Ollama connected successfully[/green]\n")
    except Exception as e:
        console.print(f"[red]✗ Ollama not running. Please start Ollama first.[/red]")
        console.print(f"[dim]Run: ollama serve[/dim]\n")
        sys.exit(1)
    
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("Select a tool", default=0)
            run_tool(choice)
        except KeyboardInterrupt:
            console.print("\n[yellow]Goodbye![/yellow]")
            break

if __name__ == "__main__":
    main()
