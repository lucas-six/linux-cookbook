# Amdahl's Law

The main idea is that when we speed up one part of a system,
the effect on the overall system performance depends on
both how significant this part was and how much it sped up.

Suppose some part of the system requires a fraction **$\alpha$** α of this time, and that
we improve its performance by a factor of **$k$**.
So speedup **$S$** (部分性能优化对整体的提速倍数):

$$ S = \frac{1}{(1-\alpha) + 2/k},  $$

When,

$$  \alpha = 部分耗时占比 $$

$$ k = 部分性能提速倍数 $$

## References

- Book: *Computer Systems: A Programmer's Perspective, Third Edition* (2016)
