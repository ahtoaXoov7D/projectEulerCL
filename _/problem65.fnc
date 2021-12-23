
                           ┌─────┐
                         ┌─┴─╖   │
      ┌──────────────────┤ % ║   │                  ╔════╗ ╓────────╖
      │                  ╘═╤═╝   │                  ║ 10 ║ ║ digsum ║
      │                    │     │                  ╚══╤═╝ ╙───┬────╜
      │                  ┌─┴─╖   │                  ┌──┴─╖     │   ┌───╖╔═══╗
      │  ┌─────╖   ┌─────┤ · ╟──┬┘           ┌──────┤ ÷% ╟─────┴───┤ = ╟╢ 0 ║
      └──┤ gcd ╟───┘     ╘═╤═╝  │            │      ╘══╤═╝         ╘═╤═╝╚═══╝
         ╘══╤══╝           │    │            │       ┌─┴─╖    ╔═══╗┌─┴─╖
          ┌─┴─╖  ┌────────┬┘    │       ┌────┴───╖   │ + ╟┐   ║ 0 ╟┤ ? ╟──┐
       ┌──┤ ? ╟──┘    ╓───┴───╖ │       │ digsum ║   ╘═╤═╝│   ╚═══╝╘═╤═╝  │
       │  ╘═╤═╝       ║  gcd  ║ │       ╘════╤═══╝     │  │          │
       │    │         ╙───┬───╜ │            └─────────┘  └──────────┘
      ─┘    │             │     │
   ╔═══╗  ┌─┴─╖           │     │
   ║ 0 ╟──┤ = ╟───────────┴─────┘
   ╚═══╝  ╘═══╝



                                 ╔═══╗
                                 ║ 2 ║
                                 ╚═╤═╝
           ╓───────╖             ┌─┴─╖
           ║  cnv  ║         ┌───┤ ≠ ║
           ╙───┬───╜         │   ╘═╤═╝
               │           ┌─┴─╖ ┌─┴─╖  ╔═══╗
 ╔═══╗  ┌───╖  │  ┌────────┤ · ╟─┤ % ╟──╢ 3 ║
 ║ 0 ╟──┤ = ╟──┴──┤        ╘═╤═╝ ╘═══╝  ╚═══╝
 ╚═══╝  ╘═╤═╝     │          │
 ╔═══╗  ┌─┴─╖     │  ╔═══╗ ┌─┴─╖
 ║ 2 ╟──┤ ? ╟──┐  │  ║ 1 ╟─┤ ? ╟┐
 ╚═══╝  ╘═╤═╝  │  │  ╚═══╝ ╘═╤═╝│
          │     ┌─┴─╖      ┌─┴─╖│                   ╔════╗
          └─────┤ · ╟──────┤ · ╟┘                   ║ 99 ║
                ╘═╤═╝      ╘═╤═╝                    ╚══╤═╝
                  │  ╔═══╗   │                 ╔═══╗┌──┴──╖┌────────╖┌──────────╖
                  │  ║ 1 ║   │                 ║ 0 ╟┤ rec ╟┤ digsum ╟┤ int→str  ╟────
                  │  ╚═╤═╝   │                 ╚═══╝╘══╤══╝╘════════╝╘══════════╝
                  │  ┌─┴─╖ ┌─┴─╖╔═══╗                ╔═╧═╗
                  │  │ + ╟─┤ × ╟╢ 2 ║                ║ 1 ║
                  │  ╘═╤═╝ ╘═══╝╚═══╝                ╚═══╝
                ┌─┴─╖┌─┴─╖╔═══╗
                │ − ╟┤ ÷ ╟╢ 3 ║
                ╘═╤═╝╘═══╝╚═══╝
                ╔═╧═╗
                ║ 2 ║
                ╚═══╝




                 ┌──────┐      ╓───────╖
                 │      ├──────╢  rec  ╟──────────┐
                 │  ┌───┴───╖  ╙───┬───╜          │
                 │  │  cnv  ║      │              │
                 │  ╘═══╤═══╝      │              │
                 │      │        ┌─┴─╖   ┌───╖    │
                 │      └────────┤ · ╟───┤ × ╟────┴┐
                 │               ╘═╤═╝   ╘═╤═╝     │
                 │                 │       │       │
                 │   ┌───╖╔═══╗    │       │   ┌───┴─────┐
   ┌─────────────┴───┤ = ╟╢ 0 ║    │ ┌───╖ │   │       ┌─┴─╖
   │                 ╘═╤═╝╚═══╝    └─┤ + ╟─┘   │       │ ÷ ╟───┐
   │                 ┌─┴─╖           ╘═╤═╝     │       ╘═╤═╝   │
   │              ┌──┤ ? ╟──┐          │   ┌───┴───╖ ┌───┘     │
   │              │  ╘═╤═╝  │          │   │  gcd  ╟─┤         │
   │              │    │               │   ╘═══╤═══╝ │         │
   │            ┌─┴─╖  │             ┌─┴───────┘   ┌─┴─╖       │
   │          ┌─┤ · ╟──┘             │      ┌──────┤ · ╟──┐    │
   │          │ ╘═╤═╝                │    ┌─┴─╖    ╘═╤═╝  │    │
 ┌─┴─╖        │   │                  └────┤ ÷ ╟──────┘    │    │
 │ − ╟┐       │   │                       ╘═══╝           │    │
 ╘═╤═╝│       │   │                                       │    │
 ╔═╧═╗│       │   ├───────────────────────────────────────┘    │
 ║ 1 ║│       │   │                                            │
 ╚═══╝│       │ ┌─┴───╖                                        │
      │       └─┤ rec ╟────────────────────────────────────────┘
      │         ╘══╤══╝
      └────────────┘
