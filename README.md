# MLAB Rendition of Point·E

The goal is to ultimately create a pipeline that allows for direct text to generation of 3D models in the context of VR scene generation. A current notion of a pipeline that we are working on is leveraging openAI's point-e system that can then be converted to meshes before being rendered in some given 3D environment.

Note that a full reference of the point-e system can be found [here](https://github.com/openai/point-e).

# Usage

Install with `pip install -e .`.

To get started with examples, see the following notebooks:

 * [image2pointcloud.ipynb](point_e/examples/image2pointcloud.ipynb) - sample a point cloud, conditioned on some example synthetic view images.
 * [text2pointcloud.ipynb](point_e/examples/text2pointcloud.ipynb) - use our small, worse quality pure text-to-3D model to produce 3D point clouds directly from text descriptions. This model's capabilities are limited, but it does understand some simple categories and colors.
 * [pointcloud2mesh.ipynb](point_e/examples/pointcloud2mesh.ipynb) - try our SDF regression model for producing meshes from point clouds.

For our P-FID and P-IS evaluation scripts, see:

 * [evaluate_pfid.py](point_e/evals/scripts/evaluate_pfid.py)
 * [evaluate_pis.py](point_e/evals/scripts/evaluate_pis.py)

For our Blender rendering code, see [blender_script.py](point_e/evals/scripts/blender_script.py)

