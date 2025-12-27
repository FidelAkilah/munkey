import Image from 'next/image';

async function getNews() {
  // Replace with your actual Django API endpoint later
  const res = await fetch('http://localhost:8000/api/news/', { cache: 'no-store' });
  return res.json();
}

export default async function HomePage() {
  // const news = await getNews(); // Uncomment when Django API is ready

  return (
    <main className="max-w-7xl mx-auto p-6">
      <header className="mb-12">
        <h1 className="text-5xl font-extrabold text-mun-blue">Global MUN Pulse</h1>
        <p className="text-slate-500 mt-2">Connecting the international circuit, from Junior to Collegiate.</p>
      </header>

      {/* Bento Grid Layout */}
      <div className="grid grid-cols-1 md:grid-cols-4 grid-rows-2 gap-6 h-auto md:h-[600px]">
        
        {/* Main Feature: Breaking News */}
        <div className="md:col-span-2 md:row-span-2 bg-slate-900 rounded-3xl p-8 text-white flex flex-col justify-end relative overflow-hidden group">
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent z-10" />
          <div className="z-20">
            <span className="bg-red-600 px-3 py-1 rounded-full text-xs font-bold">LIVE UPDATE</span>
            <h2 className="text-3xl font-bold mt-4 group-hover:text-mun-gold transition">The Rise of Regional Hubs: Why City Circuits are Merging</h2>
          </div>
        </div>

        {/* Secondary Story */}
        <div className="md:col-span-2 bg-mun-gold/10 border border-mun-gold/20 rounded-3xl p-6 flex flex-col justify-between">
          <h3 className="text-xl font-bold text-mun-blue">Junior Delegate Spotlight: The 12-Year-Old chairing UNSC</h3>
          <button className="text-mun-gold font-semibold self-start hover:underline">Read Interview →</button>
        </div>

        {/* Safe Space Quick Links */}
        <div className="bg-safe-green text-white rounded-3xl p-6">
          <h3 className="font-bold">Safe Zone</h3>
          <p className="text-sm mt-2 opacity-90">Moderated guides for Middle Schoolers.</p>
        </div>

        {/* Conference Map Card */}
        <div className="bg-slate-200 rounded-3xl p-6 flex items-center justify-center">
          <span className="text-slate-500 font-medium">Explore Global Map 🌍</span>
        </div>
      </div>
    </main>
  );
}