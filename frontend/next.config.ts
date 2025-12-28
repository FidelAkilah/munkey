import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [{ hostname: "localhost" }, { hostname: "res.cloudinary.com" }],
  },
  // Next.js 16 optimization
  reactCompiler: true, 
};

export default nextConfig;