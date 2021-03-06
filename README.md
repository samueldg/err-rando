# Rando

[![Build Status](https://travis-ci.org/samueldg/err-rando.svg?branch=master)](https://travis-ci.org/samueldg/err-rando)

**Rando** is a bot with useful random functionalities, for when taking decisions is hard or inconvenient.

## Commands

- `!cointoss` — Returns "heads" or "tails".
- `!diceroll` — Returns an integer from 1 to 6.
- `!dealcard` — Returns a random card value and suit.
- `!pick` — Picks from a user-defined list of space-sparated items.
- `!8ball` — Returns a [Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8-Ball) reply.

## Example usage

`!cointoss`:

> Lazy Dev: New support ticket in... heads I take it, tails it's yours.  
> Lazy Dev: !cointoss  
> Rando: tails  
> Unlucky Dev: Dammit!  

`!pick`:

> Hungry Guy: Where do we go for lunch today?  
> Hungry Coworker: !pick pizza thai burger sushi  
> Rando: thai  
> Hungry Guy: All right, let's do this!  

`!8ball`:

> Insecure Dev: !8ball Should I deploy to prod this Friday?  
> Rando: My sources say no  

## Installation

Rando has no dependencies, so it can be installed easily using the steps described in Errbot's documentation [Installing plugins](http://errbot.io/en/latest/user_guide/administration.html#installing-plugins) section.

## Contribute

Pull requests and issues are welcome!
