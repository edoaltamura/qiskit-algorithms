# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2024, 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Basin hopping optimizer."""

from __future__ import annotations

from .scipy_optimizer import SciPyOptimizer


class BasinHopping(SciPyOptimizer):  # pylint: disable=invalid-name

    _OPTIONS = ["niter", "T", "stepsize", "target_accept_rate", "stepwise_factor"]

    # pylint: disable=unused-argument
    def __init__(
        self,
        niter: int = 100,
        T: float = 1.0,
        stepsize: float = 0.5,
        target_accept_rate: float = 0.5,
        stepwise_factor: float = 0.9,
        options: dict | None = None,
        **kwargs,
    ):


        if options is None:
            options = {}
        for k, v in list(locals().items()):
            if k in self._OPTIONS:
                options[k] = v
        super().__init__(
            method="basinhopping",
            options=options,
            **kwargs,
        )
