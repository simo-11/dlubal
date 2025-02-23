# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:09:01 2025

@author: simon
"""
import dlubal.api.rfem as rfem

def define_structure() -> list:
    """Define and return a list of structural objects."""

    inf = float('inf')

    return [
        # Define material
        rfem.structure_core.Material(no=1, name='S235'),

        # Define section
        rfem.structure_core.Section(no=1, name='HE 300 A', material=1),

        # Define nodes
        rfem.structure_core.Node(no=1),
        rfem.structure_core.Node(no=2, coordinate_1=6.0),

        # Define line
        rfem.structure_core.Line(no=1, definition_nodes=[1, 2]),

        # Define member
        rfem.structure_core.Member(no=1, line=1, section_start=1),

        # Define nodal support at Node 1 (fully fixed)
        rfem.types_for_nodes.NodalSupport(
            no=1,
            nodes=[1],
            spring_x=inf, spring_y=inf, spring_z=inf,
            rotational_restraint_x=inf,
            rotational_restraint_y=inf,
            rotational_restraint_z=inf
        ),
    ]

def define_loading() -> list:
    """Define and return a list of loading objects."""

    return [
        # Static analysis settings
        rfem.loading.StaticAnalysisSettings(
            no=1,
            analysis_type=rfem.loading.StaticAnalysisSettingsAnalysisType.
            STATIC_ANALYSIS_SETTINGS_ANALYSIS_TYPE_GEOMETRICALLY_LINEAR
        ),

        # Define load cases
        rfem.loading.LoadCase(no=1, static_analysis_settings=1),
        rfem.loading.LoadCase(no=2, static_analysis_settings=1),

        # Define nodal loads
        rfem.loads.NodalLoad(
            no=1,
            load_case=1,
            nodes=[2],
            load_type=rfem.loads.NodalLoadLoadType.
            NODAL_LOAD_LOAD_TYPE_COMPONENTS,
            components_force_y=5000,  # Force in Y direction (N)
            components_force_z=100000  # Force in Z direction (N)
        ),
        rfem.loads.NodalLoad(
            no=2,
            load_case=2,
            nodes=[2],
            load_type=rfem.loads.NodalLoadLoadType.
            NODAL_LOAD_LOAD_TYPE_COMPONENTS,
            components_force_y=20000,
            components_force_z=5000
        ),

        # Define design situation
        rfem.loading.DesignSituation(
            no=1,
            design_situation_type="DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10"
        ),

        # Define load combination
        rfem.loading.LoadCombination(
            no=1,
            combination_rule_str="LC1+1.35*LC2",
            design_situation=1
        ),
    ]

def main() -> None:
    """Runs the structural analysis example."""

    with rfem.Application(api_key_name="lut_student") as rfem_app:

        # Step 1: Create a new model
        rfem_app.create_model(name='cantilever')

        # Step 2: Clear existing objects
        rfem_app.delete_all_objects()

        # Step 3: Define and create all objects
        objects = define_structure() + define_loading()
        rfem_app.create_object_list(objects)

        # Step 4: Retrieve and display information about a specific member
        member = rfem_app.get_object(rfem.structure_core.Member(no=1))
        print("Member Details:\n", member)

        # Step 5: Run Plausibility check
        plausibility_check = rfem_app.plausibility_check(
            type=rfem.PLAUSIBILITY_CHECK_CALCULATION,
            skip_warnings=True
        )
        print("Plausibility Check:\n", plausibility_check)

        # Step 6: Perform calculation
        calculation = rfem_app.calculate_all(skip_warnings=True)
        print("Calculation Info:\n", calculation)


if __name__ == "__main__":
    main()
