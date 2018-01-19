import os.path as op
from shutil import copyfile
import fileinput

working_dir = op.dirname(__file__)

# Chapter Registration
source = op.join(working_dir, '../RegistrationLaTeX/Chapters')
destination = op.join(working_dir, './Chapters/02_Registration/Chapters/')

tex_files = { 'Abstract.tex',
			 'Acknowledgements.tex',
			 'Appendix.tex',
			 'Discussion.tex',
			 'Introduction.tex',
			 'Methods.tex',
			 'Results.tex',
			 'Figures/AAD.tex',
			 'Figures/CubeDivision.tex',
			 'Figures/EpiRegistration.tex',
			 'Figures/FlashRegistration.tex',
			 'Figures/QrCodes.tex',
			 'Figures/RegistrationExamples.tex',
			 'Figures/RegistrationHistogram.tex'}
for file in tex_files:
	copyfile(op.join(source, file), op.join(destination, file))
	
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('\input{', '\input{./Chapters/02_Registration/').replace('\citep{', '\cite{'), end='')
		
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('clip=true]{', 'clip=true]{./Chapters/02_Registration/Images/'), end='')
			
source = op.join(working_dir, '../RegistrationLaTeX/Images')
destination = op.join(working_dir, './Chapters/02_Registration/Images/')
figure_files = {
  			   'AAD.eps',
  			   'WorkflowSchematic.eps',
			   'EpiRegistration.eps',
			   'FLASH_registration.eps',
			   'QRCodes.eps',
			   'SupplementRegistrations.eps',
			   'Histograms.eps'}
for file in figure_files:
	copyfile(op.join(source, file), op.join(destination, file))
    
		
# Chapter GLM
source = op.join(working_dir, '../GlmLaTeX/Chapters')
destination = op.join(working_dir, './Chapters/03_GLM/Chapters/')

tex_files = { 'Abstract.tex',
			 'Acknowledgements.tex',
			 'Appendix01.tex',
			 'Appendix02.tex',
			 'Discussion.tex',
			 'Introduction.tex',
			 'Methods.tex',
			 'Results.tex',
			 'SupplementaryMaterial.tex',
			 'Theory.tex',
			 'Figures/Cube.tex',
			 'Figures/ExVivoRoi.tex',
			 'Figures/InVivoResults.tex',
			 'Figures/InVivoRoi.tex',
			 'Figures/SimulationProcedure.tex',
			 'Figures/SimulationResults.tex',
			 'Figures/SimulationVolume.tex'}
for file in tex_files:
	copyfile(op.join(source, file), op.join(destination, file))
	
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('\input{', '\input{./Chapters/03_GLM/').replace('\citep{', '\cite{'), end='')
		
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('clip=true]{', 'clip=true]{./Chapters/03_GLM/'), end='')
			
source = op.join(working_dir, '../GlmLaTeX/Images')
destination = op.join(working_dir, './Chapters/03_GLM/Images/')
figure_files = {
  			   'Cube.eps',
  			   'Simulation.eps',
			   'LayeringSimulation.eps',
			   'LayeringInVivo.eps',
			   'PointSpread.eps',
			   'PointSpreadMatrices.eps',
			   'Quadrilateral.eps',
			   'MichielData.eps',
			   'ProfileComparisons.eps'}
for file in figure_files:
	copyfile(op.join(source, file), op.join(destination, file))
    

# Chapter Attention
source = op.join(working_dir, '../LayerAttentionLaTeX/Chapters')
destination = op.join(working_dir, './Chapters/04_Attention/Chapters/')

tex_files = { 'Abstract.tex',
			 'Acknowledgements.tex',
			 'AuthorContributions.tex',
			 'Discussion.tex',
			 'Introduction.tex',
			 'Methods.tex',
			 'Results.tex',
			 'SupplementaryMaterials.tex',
			 'Figures/FigureExampleBrain.tex',
			 'Figures/FigureExperiment.tex',
			 'Figures/FigureLayerResults.tex',
			 'Figures/FigureLayerResults_4Layers.tex',
			 'Figures/FigureLayerResults_300Vertices.tex',
			 'Figures/FigureLayerResults_900Vertices.tex',
			 'Figures/FigureLayerResults_interpolation.tex',
			 'Figures/FigureLayerResults_plusAttention.tex',
			 'Figures/FigureRoiResults.tex'}
for file in tex_files:
	copyfile(op.join(source, file), op.join(destination, file))
	
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('\input{', '\input{./Chapters/04_Attention/').replace('\citep{', '\cite{').replace('\citet{', '\cite{'), end='')
		
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('clip=true]{', 'clip=true]{./Chapters/04_Attention/Images/'), end='')
			
source = op.join(working_dir, '../LayerAttentionLaTeX/Images')
destination = op.join(working_dir, './Chapters/04_Attention/Images/')
figure_files = {
  			   'ExampleBrain.eps',
  			   'Experiment.eps',
			   'LayerResults.eps',
			   'RoiResults.eps',
			   'SM_LayerResults_4Layers.eps',
			   'SM_LayerResults_300vertices.eps',
			   'SM_LayerResults_900vertices.eps',
			   'SM_LayerResults_interpolation.eps',
			   'SM_LayerResults_plusAttention.eps'}
for file in figure_files:
	copyfile(op.join(source, file), op.join(destination, file))
    

# Chapter Porcupine
source = op.join(working_dir, '../PorcupineLaTeX/Chapters')
destination = op.join(working_dir, './Chapters/05_Porcupine/Chapters/')

tex_files = { 'Abstract.tex',
			 'Acknowledgements.tex',
			 'Appendix.tex',
			 'AuthorContributions.tex',
			 'Introduction.tex',
			 'Methods.tex',
			 'Results.tex',
			 'Discussion.tex',
			 'Figures/FigureEditor.tex',
			 'Figures/FigureExampleAdvanced.tex',
			 'Figures/FigureExampleSimple.tex'}
for file in tex_files:
	copyfile(op.join(source, file), op.join(destination, file))
	
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('\input{', '\input{./Chapters/05_Porcupine/').replace('\citep{', '\cite{'), end='')
		
for file in tex_files:
	with fileinput.FileInput(op.join(destination, file), inplace=True) as file:
		for line in file:
			print(line.replace('clip=true]{', 'clip=true]{./Chapters/05_Porcupine/'), end='')
			
			
source = op.join(working_dir, '../PorcupineLaTeX/Images')
destination = op.join(working_dir, './Chapters/05_Porcupine/Images/')
figure_files = {
  			   'gui_showcase.pdf',
  			   'pork_graph.pdf',
			   'pork_py.pdf'}
for file in figure_files:
	copyfile(op.join(source, file), op.join(destination, file))




