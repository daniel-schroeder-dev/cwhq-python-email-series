## Question

The following function comes from a game and determines whether to end the game based on the value of the `player_health` variable. It's supposed to receive the `player_health` as an argument and then run a function called `end_game()` if there is no health left.

Currently, this function doesn't work as it's supposed to. Find and fix the errors so the function works correctly.

```python
def check_player_health()
if player_health > 0:
    end_game()

```

## Answer

```python
def check_player_health(player_health):
    if player_health <= 0:
        end_game()

```

## Explanation

The first error is the missing `player_health` parameter that the function is supposed to use.

```python
                # Need to add the parameter
def check_player_health(player_health)
if player_health > 0:
    end_game()

```

Next, the function header is missing the final colon (`:`).

```python
                # Need to add the colon
def check_player_health(player_health):
if player_health > 0:
    end_game()

```

When defining a function, all statements that should be _inside_ the function must be indented. To fix the indentation issues, we need to indent the conditional statement header and body.

```python
def check_player_health(player_health):
    # Indentation is how Python knows this is part of the
    # function definition
    if player_health > 0:
        end_game()

```

The `end_game()` function should only be called when the player has no health, so we should be checking if the `player_health` is less than or equal to 0.

```python
def check_player_health(player_health):
    # Make sure the conditional statement only runs if
    # there is no health
    if player_health <= 0:
        end_game()

```

## Resources

-   [The CodeWizardsHQ Docs - User-Defined Functions](https://docs.codewizardshq.com/python/python-language/#user-defined-functions)
