import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      { hostname: "localhost" },
      { hostname: "res.cloudinary.com" },
      { hostname: "mun-global.onrender.com" },
      { hostname: "i.imgur.com" },
    ],
  },
  // Next.js 16 optimization
  reactCompiler: true, 
};

export default nextConfig;