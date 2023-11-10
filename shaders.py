# Leguaje GLSL (Graphics Library Shader Languaje)

vertex_shader = """
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 outNormals;

void main() {
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position,1.0);
    UVs = texcoords;
    outNormals = (modelMatrix * vec4(normals,0.0)).xyz;
}
"""

fragment_shader = """
#version 450 core

layout(binding = 0) uniform sampler2D tex;

uniform vec3 dirLight;

in vec2 UVs;
in vec3 outNormals;

out vec4 fragColor;

void main() {
    float intensity = dot(outNormals, -dirLight);
    intensity = min(1,intensity);
    intensity = max(0,intensity);
    fragColor = texture(tex, UVs) ;
}
"""

noise_fragment_shader = """
#version 450 core

layout(binding = 0) uniform sampler2D tex;

in vec2 UVs;
in vec3 outNormals;

float rand(vec2 co){
    return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    float noiseFactor = rand(UVs * 100.0);

    vec4 originalColor = texture(tex, UVs); //og texture color

    // Modulate the original color with noise
    vec4 noiseColor = originalColor * (1.0 - noiseFactor * 0.5);

    gl_FragColor = noiseColor;
}
"""

ballon_fragment_shader = """
#version 450 core

layout(binding = 0) uniform sampler2D tex;

in vec2 UVs;
in vec3 outNormals;

uniform float time; // Time uniform for animation

out vec4 fragColor;

void main() {
    vec4 originalColor = texture(tex, UVs);

    float frequency = 3.0; 
    float amplitude = 0.01;

    float xDisplacement = amplitude * sin(UVs.x * frequency + time);
    float yDisplacement = amplitude * sin(UVs.y * frequency + time);

    vec2 distortedUVs = UVs + vec2(xDisplacement, yDisplacement);
    vec4 waterColor = texture(tex, distortedUVs);
    fragColor = mix(originalColor, waterColor, 0.5); // Adjust the blending factor as needed
}
"""

ballon_vertex_shader = """
#version 450 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texcoords;
layout(location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec2 UVs;
out vec3 outNormals;
out vec3 displacedPosition; 
out vec4 vertexColor; 

uniform float time; // Time uniform for animation

void main() {
    float rippleAmplitude = 0.1; 
    float rippleFrequency = 3.0; 

    vec3 rippleOffset = normals * rippleAmplitude * sin(time * rippleFrequency);

    displacedPosition = position + rippleOffset;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(displacedPosition, 1.0);

    UVs = texcoords;
    outNormals = (modelMatrix * vec4(normals, 0.0)).xyz;

    vec3 baseColor = vec3(0.0, 0.8, 1.0); 
    float colorFactor = 0.5 + 0.5 * sin(time * 3.0); 

    vertexColor = vec4(baseColor * colorFactor, 1.0);
}
"""

color_fragment_shader = """
#version 450 core

in vec3 outNormals;

uniform float time;

out vec4 fragColor;

void main(){
  float theta = time*10.0;
  
  vec3 direction1 = vec3(cos(theta),0,sin(theta)); 
  vec3 direction2 = vec3(sin(theta),0,cos(theta));
  vec3 direction3 = vec3(cos(theta),sin(theta),cos(theta));
  
  float diffuserColor1 = pow(dot(outNormals,direction1),2.0);
  float diffuserColor2 = pow(dot(outNormals,direction2),2.0);
  float diffuserColor3 = pow(dot(outNormals,direction3),2.0);
  
  vec3 first_color = diffuserColor1 * vec3(1,0.5,0);
  vec3 second_color = diffuserColor2 * vec3(0,0,1);
  vec3 third_color = diffuserColor3 * vec3(0.4,0,1);
  
  fragColor = vec4(first_color + second_color + third_color, 1.0);
}
"""