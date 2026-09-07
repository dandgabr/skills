# 🛠️ Guia Prático de Design Engineering & Artesanalidade Frontend (Craft UI)

Este guia fornece padrões de código de alta fidelidade e snippets prontos para produção para des-templatização, física de animações, superfícies táteis e acessibilidade avançada.

---

## 1. Des-templatização de Componentes: O Padrão Wrapper Autoral

Evite usar diretamente o componente cru do shadcn nas páginas. Crie um wrapper autoral que adiciona estados táteis, microinterações e tokens semânticos:

```tsx
// components/craft/AppButton.tsx
import * as React from "react";
import { motion, HTMLMotionProps } from "framer-motion";

export interface AppButtonProps extends HTMLMotionProps<"button"> {
  variant?: "primary" | "secondary" | "subtle" | "brutalist";
  size?: "sm" | "md" | "lg";
  children: React.ReactNode;
}

export const AppButton = React.forwardRef<HTMLButtonElement, AppButtonProps>(
  ({ variant = "primary", size = "md", className = "", children, ...props }, ref) => {
    const sizeClasses = {
      sm: "h-8 px-3 text-xs gap-1.5",
      md: "h-10 px-4 text-sm gap-2",
      lg: "h-12 px-6 text-base gap-2.5"
    }[size];

    const variantClasses = {
      primary:
        "bg-white text-black font-medium border border-transparent shadow-sm hover:bg-neutral-200 active:bg-neutral-300",
      secondary:
        "bg-[#141618] text-[#e1e4ea] border border-[rgba(255,255,255,0.08)] hover:border-[rgba(255,255,255,0.18)] hover:bg-[#1a1d20]",
      subtle:
        "bg-transparent text-neutral-400 hover:text-white hover:bg-[rgba(255,255,255,0.04)]",
      brutalist:
        "bg-[#FFE600] text-black font-bold border-2 border-black shadow-[3px_3px_0px_#000] hover:translate-x-[1px] hover:translate-y-[1px] hover:shadow-[2px_2px_0px_#000] active:translate-x-[3px] active:translate-y-[3px] active:shadow-none"
    }[variant];

    return (
      <motion.button
        ref={ref}
        whileTap={variant !== "brutalist" ? { scale: 0.98 } : undefined}
        transition={{ type: "spring", stiffness: 500, damping: 25 }}
        className={`inline-flex items-center justify-center rounded-[2px] tracking-tight transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-[#080A0A] disabled:opacity-50 disabled:pointer-events-none ${sizeClasses} ${variantClasses} ${className}`}
        {...props}
      >
        {children}
      </motion.button>
    );
  }
);

AppButton.displayName = "AppButton";
```

---

## 2. Injeção de Ruído Analógico Performático via SVG Data-URI

Adicione textura táctil que quebra a esterilidade do canvas digital sem afetar Core Web Vitals:

```css
/* styles/craft-textures.css */

/* Camada de granulação com Perlin Noise SVG sem requisição de rede */
.craft-grain-overlay {
  position: relative;
}

.craft-grain-overlay::after {
  content: "";
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.045;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  mix-blend-mode: overlay;
}
```

---

## 3. Arquitetura de Molas no Framer Motion (Spring Physics)

Molas calibradas com rigor matemático para movimentos firmes, elegantes e sem "quique" de template:

```typescript
// lib/animation/springs.ts

export const springPhysics = {
  // Mola para modais, dropdowns e abas (alta firmeza e sem oscilação)
  interfaceSnappy: {
    type: "spring" as const,
    stiffness: 420,
    damping: 34,
    mass: 0.8
  },
  // Mola para revelação sequencial de cards (suave, fluida)
  contentGentle: {
    type: "spring" as const,
    stiffness: 280,
    damping: 26,
    mass: 1.0
  },
  // Mola tátil para micro-estados e botões
  microPress: {
    type: "spring" as const,
    stiffness: 550,
    damping: 22,
    mass: 0.4
  }
};
```

---

## 4. Card com Hairline Border e Surface Ladder

```tsx
// components/craft/TactileCard.tsx
import React from "react";

interface TactileCardProps {
  level?: 1 | 2 | 3;
  children: React.ReactNode;
  className?: string;
}

export function TactileCard({ level = 1, children, className = "" }: TactileCardProps) {
  // Surface ladder: luminância crescente conforme o nível de elevação
  const levelStyles = {
    1: "bg-[#0c0d0e] border-[rgba(255,255,255,0.06)] hover:border-[rgba(255,255,255,0.12)]",
    2: "bg-[#141618] border-[rgba(255,255,255,0.08)] hover:border-[rgba(255,255,255,0.16)]",
    3: "bg-[#1c1f22] border-[rgba(255,255,255,0.12)] shadow-xl"
  }[level];

  return (
    <div
      className={`rounded-[2px] border p-6 transition-all duration-200 ${levelStyles} ${className}`}
    >
      {children}
    </div>
  );
}
```
