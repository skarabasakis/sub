# sub

A command line subscription manager that helps you track your subscription-related expenses.

## Features

- track your active subscriptions

```shell
$ sub to netflix.com for 12.99/m
$ sub to spotify.com for 7.99/m since 20 September 2023 until August 2024
$ sub to hulu.com for 99.99/y since March 10
$ sub to hellomobile.com for 45/3m since last month

$ sub list
○ spotify.com                   7.99 / month      2023-09-20 - 2024-08-13
● hulu.com                     99.99 / year       2024-03-10 -
● hellomobile.com              45.00 / 3 months   2024-11-13 -
● netflix.com                  12.99 / month      2024-12-13 -
```

- cancel subscriptions

```shell
$ sub cancel hulu.com
$ sub list
○ spotify.com                   7.99 / month      2023-09-20 - 2024-08-13
○ hulu.com                     99.99 / year       2024-03-10 - 2024-12-13
● hellomobile.com              45.00 / 3 months   2024-11-13 -
● netflix.com                  12.99 / month      2024-12-13 -
```

- monitor how much you are spending

```shell
$ sub total
232.88
$ sub total spotify.com
87.89
$ sub total since January 2024
200.92
$ sub payments since 1 Jan 2024
2024-01-20      7.99 spotify.com
2024-02-20      7.99 spotify.com
2024-03-10     99.99 hulu.com
...
2024-11-13     45.00 hellomobile.com
```

- plan your subscription budget

```shell
$ sub payments since today until March 2025
2024-12-13     12.99 netflix.com
2025-01-13     12.99 netflix.com
2025-02-13     12.99 netflix.com
2025-02-13     45.00 hellomobile.com
$ sub total since today until March 2025
83.97
```

## Installation

**Docker**

```shell
docker pull skarabasakis/sub
# add an alias to your shell profile (e.g. .bashrc, .zshrc)
alias sub="docker run --name sub --rm -v sub:/data/ skarabasakis/sub"
```
