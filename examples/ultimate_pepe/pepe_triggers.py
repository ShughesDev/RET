#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:57:09 2023

@author: Shugsy
"""
###### Imports
from __future__ import annotations
### Standard


### RET
from mesa_ret.agents.agent import RetAgent
from mesa_ret.orders.order import Trigger
from mesa_ret.sensing.perceivedworld import (
    AgentsAt,
    And,
    FriendlyAgents,
    HostileAgents,
    IdentifiedAgents,
    UnknownAgents,
    NearbyAgents,
)

###### Classes

def DistanceCalculator(p, q):
    dx = q[0] - p[0]
    dy = q[1] - p[1]
    
    c2 = dx**2 + dy**2
    
    c = c2 ** 0.5
    
    return c

class HostileAgentInRangeTrigger(Trigger):
    def __init__(self, rnge: float, agent: RetAgent) -> None:
        super().__init__(log = True)
        self._range = rnge
        self._agent = agent
    
    def __str__(self) -> str:
        return "Identified hostile agent(s) in range trigger."
    
    def _check_condition(self, checker: RetAgent) -> bool:
        """Check for identified hostile agents at position."""
        perceived_agents = checker.perceived_world.get_perceived_agents(
            And(
                [
                    IdentifiedAgents(),
                    NearbyAgents(
                        distance_calculator = DistanceCalculator,
                        agent = self._agent,
                        range = self._range,
                        ),
                    HostileAgents(),
                ]
            )
        )
        
        return len(perceived_agents) > 0

    def get_new_instance(self) -> HostileAgentInRangeTrigger:
        """Get new instance of Trigger."""
        return HostileAgentInRangeTrigger(
            rnge = self._range,
            agent = self._agent,
        )